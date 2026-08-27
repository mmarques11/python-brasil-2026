# Aula Python Brasil

## Instalando o `uv`

O `uv` é a ferramenta que usaremos para instalar o Python, criar o ambiente
virtual e gerenciar as dependências do projeto.

### Windows

1. Abra o **PowerShell**.

2. Execute o instalador oficial:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. Feche e abra o PowerShell novamente para atualizar o `PATH`.

4. Confirme que a instalação foi concluída:

   ```powershell
   uv --version
   ```

Se o comando mostrar a versão instalada, o `uv` está pronto para uso.

Como alternativa, quem utiliza o **WinGet** pode instalar o `uv` com:

```powershell
winget install --id=astral-sh.uv -e
```

### macOS e Linux

1. Abra o terminal.

2. Execute o instalador oficial:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Feche e abra o terminal novamente.

4. Confirme a instalação:

   ```bash
   uv --version
   ```

## Próximo passo

Com o `uv` instalado, já podemos criar e executar projetos Python sem precisar
instalar o Python separadamente. O `uv` baixa automaticamente uma versão
compatível do Python quando ela for necessária.

Dentro da pasta do projeto, execute:

```powershell
uv sync
```

Esse comando cria o ambiente virtual e instala as dependências definidas no
`pyproject.toml`, respeitando as versões registradas no `uv.lock` quando esse
arquivo estiver presente.

Para conhecer outras formas de instalação, consulte a
[documentação oficial do uv](https://docs.astral.sh/uv/getting-started/installation/).
