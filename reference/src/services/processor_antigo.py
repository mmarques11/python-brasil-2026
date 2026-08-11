import re
from datetime import datetime
from time import perf_counter

from playwright.sync_api import Playwright, sync_playwright, expect

ROUND_MAX = 10

def run(playwright: Playwright) -> None:
    round_atual = 1
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rpachallenge.com/")
    page.get_by_role("button", name="Start").click()

    while round_atual <= ROUND_MAX:
        page.locator("label", has_text="Email").locator("xpath=following-sibling::input").fill("mateus.dev@gmail.com")
        page.locator("label", has_text="Address").locator("xpath=following-sibling::input").fill("rua dos coqueiros, 555")
        page.locator("label", has_text="First Name").locator("xpath=following-sibling::input").fill("Mateus")
        page.locator("label", has_text="Company Name").locator("xpath=following-sibling::input").fill("Join4")
        page.locator("label", has_text="Last Name").locator("xpath=following-sibling::input").fill("Marques")
        page.locator("label", has_text="Role in Company").locator("xpath=following-sibling::input").fill("Consultor")
        page.locator("label", has_text="Phone Number").locator("xpath=following-sibling::input").fill("149988776655")
        page.get_by_role("button", name="Submit").click()
        round_atual += 1

    # ---------------------
    context.close()
    browser.close()

def main() -> None:
    inicio = datetime.now()
    temporizador = perf_counter()
    print(f'Execução iniciada em: {inicio:%d/%m/%Y %H:%M:%S}')

    try:
        with sync_playwright() as playwright:
            run(playwright)
    finally:
        fim = datetime.now()
        duracao = perf_counter() - temporizador
        print(f'Execução finalizada em: {fim:%d/%m/%Y %H:%M:%S}')
        print(f'Tempo total: {duracao:.2f} segundos')


if __name__ == '__main__':
    main()
