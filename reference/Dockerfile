# Usar a imagem oficial com Chromium e dependências do Playwright.
# Manter a versão igual à versão do Playwright registrada no uv.lock.
FROM mcr.microsoft.com/playwright/python:v1.61.0-noble

# Copiar os executáveis do uv da imagem oficial.
COPY --from=ghcr.io/astral-sh/uv:0.11.26 /uv /uvx /bin/

# Configurar a execução dentro do contêiner:
# - HEADLESS: executa o navegador sem abrir uma janela gráfica;
# - PYTHONDONTWRITEBYTECODE: não cria arquivos .pyc;
# - PYTHONUNBUFFERED: exibe os logs imediatamente;
# - UV_COMPILE_BYTECODE: compila as dependências para acelerar a inicialização;
# - UV_LINK_MODE: copia os pacotes para o ambiente virtual.
ENV HEADLESS=true \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Definir /app como diretório dos próximos comandos.
WORKDIR /app

# Copiar primeiro os arquivos de dependências para aproveitar o cache do Docker.
# Reutilizar esta camada quando apenas o código mudar.
COPY pyproject.toml uv.lock README.md ./

# Criar o ambiente virtual e instalar exatamente as versões do uv.lock.
RUN uv sync --frozen --no-dev --no-install-project

# Copiar o código-fonte e os dados necessários.
COPY main.py ./
COPY src ./src
COPY data ./data

# Executar este comando ao iniciar o contêiner.
CMD ["/app/.venv/bin/python", "main.py"]
