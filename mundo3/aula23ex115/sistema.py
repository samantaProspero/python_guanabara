# 115a: Vamos criar um menu em Python, usando modularização.
# 115b: Vamos ver como fazer acesso a arquivos usando o Python.
# 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
from mundo3.aula23ex115.lib.interface import *

while True:
    resp = menu(['Ver Pessoas cadastradas', 'cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1 or resp == 2:
        cabecalho(f'Opção {resp}')
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0:31mErro! Digite uma opção válida!\033[m')
