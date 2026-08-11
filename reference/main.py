import asyncio
from datetime import datetime
from time import perf_counter

from src.services.processor_novo import executar_processamento


async def main() -> None:
    inicio = datetime.now()
    temporizador = perf_counter()
    print(f'Execução iniciada em: {inicio:%d/%m/%Y %H:%M:%S}')

    try:
        await executar_processamento()
    finally:
        fim = datetime.now()
        duracao = perf_counter() - temporizador
        print(f'Execução finalizada em: {fim:%d/%m/%Y %H:%M:%S}')
        print(f'Tempo total: {duracao:.2f} segundos')


if __name__ == '__main__':
    asyncio.run(main())
