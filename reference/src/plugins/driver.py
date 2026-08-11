import asyncio
from dataclasses import dataclass
from typing import Literal, Optional

from playwright.async_api import (
    Browser,
    BrowserContext,
    BrowserType,
    Page,
    Playwright,
    async_playwright,
)


BrowserName = Literal['chromium', 'firefox', 'webkit']


@dataclass(frozen=True)
class PlaywrightDriverConfig:
    navegador: BrowserName = 'chromium'
    headless: bool = False
    slow_mo: int = 10000
    timeout_ms: int = 45000
    viewport_width: int = 1366
    viewport_height: int = 768


class DriverPlaywright:
    def __init__(
        self,
        browser_name: BrowserName = 'chromium',
        headless: bool = False,
        slow_mo: int = 0,
        base_url: Optional[str] = None,
    ):
        self.config = PlaywrightDriverConfig(
            navegador=browser_name,
            headless=headless,
            slow_mo=slow_mo,
        )
        self._playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self.base_url = base_url
        self._lifecycle_lock = asyncio.Lock()

    def _get_browser_launcher(self) -> BrowserType:
        if not self._playwright:
            raise RuntimeError('O Playwright ainda não foi inicializado.')

        if self.config.navegador == 'chromium':
            return self._playwright.chromium
        if self.config.navegador == 'firefox':
            return self._playwright.firefox
        if self.config.navegador == 'webkit':
            return self._playwright.webkit

        raise ValueError("Navegador não suportado. Use 'chromium', 'firefox' ou 'webkit'.")

    async def iniciar_driver(self) -> Browser:
        # Evita que a mesma instância seja iniciada duas vezes ao mesmo tempo.
        async with self._lifecycle_lock:
            if self._playwright is not None:
                raise RuntimeError('O driver Playwright já foi inicializado.')

            self._playwright = await async_playwright().start()
            try:
                launcher = self._get_browser_launcher()

                browser = await launcher.launch(
                    headless=self.config.headless,
                    slow_mo=self.config.slow_mo,
                )
                self.browser = browser
            except Exception:
                await self._fechar_recursos()
                raise

            return browser

    async def novo_contexto(self) -> BrowserContext:
        async with self._lifecycle_lock:
            if not self.browser:
                raise RuntimeError('O browser Playwright ainda não foi inicializado.')

            context = await self.browser.new_context(
                base_url=self.base_url,
                accept_downloads=True,
                viewport={
                    'width': self.config.viewport_width,
                    'height': self.config.viewport_height,
                },
            )
            context.set_default_timeout(self.config.timeout_ms)
            context.set_default_navigation_timeout(self.config.timeout_ms)
            return context

    async def nova_pagina(self, context: BrowserContext) -> Page:
        return await context.new_page()

    async def fechar_driver(self) -> None:
        # Se uma inicialização estiver em andamento, espera ela terminar.
        async with self._lifecycle_lock:
            await self._fechar_recursos()

    async def _fechar_recursos(self) -> None:
        # Fechar o browser também fecha seus contextos e páginas.
        try:
            if self.browser:
                await self.browser.close()
        finally:
            try:
                if self._playwright:
                    await self._playwright.stop()
            finally:
                self.browser = None
                self._playwright = None
