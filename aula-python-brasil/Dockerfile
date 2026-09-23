# A versão da imagem deve acompanhar a versão do Playwright no uv.lock.
FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

# Copiar os executáveis do uv da imagem oficial, usando uma versão fixa.
COPY --from=ghcr.io/astral-sh/uv:0.12.17 /uv /uvx /bin/

ENV HEADLESS=true \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Instalar primeiro as dependências para aproveitar o cache do Docker.
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --no-install-project

# Copiar o código da aplicação.
COPY main.py __init__.py ./
COPY src ./src

CMD ["/app/.venv/bin/python", "main.py"]
