# Reference

Automação em Python que preenche o desafio do RPA Challenge usando Playwright.

## Execução local

Instale as dependências e o Chromium:

```powershell
uv sync
uv run playwright install chromium
```

Execute o projeto:

```powershell
uv run python main.py
```

Por padrão, a execução local abre o navegador. Para executar sem interface gráfica:

```powershell
$env:HEADLESS = "true"
uv run python main.py
```

## Execução com Docker

Construa e execute com Docker Compose:

```powershell
docker compose up --build
```

O diretório `data` local é montado como somente leitura em `/app/data`. Assim, a
planilha `data/dados.xlsx` pode ser atualizada sem reconstruir a imagem.

Para executar novamente sem reconstruir:

```powershell
docker compose run --rm reference
```
