
# Funções: 2ª parte
# Interactive Help
# help e doc:
# 1ª maneira: help(funcionalidade) ou print(funcionalidade.__doc__) no arquivo e depois run
# 2ª maneira: no console do PyCharm help(), e depois digita a funcionalidade q deseja pesquisar
#
# docstring é uma string de documentação,
# em uma função criada pela pessoa, a docstring é uma explicação, um manual da função
# é feita em uma linha abaixo da def encapsulada por três aspas duplas
#
# def contador(i, f, p):
#     """
#     ->Faz uma contagem e mostra na tela
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM!')
#
#
# contador(1, 10, 2)
"""
parâmetros opcionais:
def soma(a, b, c=0): c é opcional
    s = a + b + c
    print(s) 
soma(3, 2)
escopo de variáveis: 


def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')

n1 = 2
funcao()
print(f'n1 fora vale {n1}')
# retorno:(o n1 de dentro e o n1 de fora são independentes)
# n1 dentro vale 4
# n1 fora vale 2

# para ligar os dois n1 é "global  n1" dentro da função:
# assim a função irá alterar o valor no n1 de fora também
def funcao():
    global n1
    n1 = 4
    print(f'n1 dentro vale {n1}')

n1 = 2
funcao()
print(f'n1 fora vale {n1}')
Retornando valores:

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
resp = soma(3, 2, 5)
print(resp)
print(soma(3, 2, 5))

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um número: '))
print(f'{n}! = {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
"""

# 101: Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

"""
def voto(ano):
    from datetime import date
    global idade
    idade = date.today().year - ano
    if idade < 16:
      return f'Com {idade} anos: NÂO VOTA'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'
    
    
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
"""
# 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# def fatorial(num=1, show=False):
#     """
#     -> Calcula o Fatorial de um número.
#     :param num: O número a ser calculado.
#     :param show: (opcional) Mostrar ou não a conta.
#     :return: O valor do Fatorial de um número num
#     """
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#         if show == True:
#             if c != 1:
#                 print(f'{c} ', end='x ')
#             else:
#                 print(f'{c} ', end='= ')
#
#     return f
#
#
# print(fatorial(5, True))
# print(fatorial(4, False))
# help(fatorial)


# 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
"""
nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

if not gols.isnumeric():
    gols = '0'
if nome.strip() == '':
    nome = '<desconhecido>'
def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
ficha(nome, gols)
"""
# 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

"""
def leiaInt(msg):
    a = input(msg)
    while not a.isnumeric():
        print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
        a = input(msg)
    return f'Você acabou de digitar o número {a}.'

n = leiaInt('Digite um n: ')
print(n)

"""
# 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

# dicionario ={}
# def notas(*num, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param num: Uma ou mais notas dos alunos.
#     :param sit: valor opcional, indica se deve ou não adicionar a situação
#     :return: dicionário com várias informações sobre o aluno.
#     """
#     dicionario['total'] = len(num)
#     dicionario['maior'] = max(num)
#     dicionario['menor'] = min(num)
#     media = sum(num)/len(num)
#     dicionario['media'] = media
#     if sit:
#         if media > 7:
#             resp = 'BOA'
#         elif media < 5:
#             resp = 'RUIM'
#         else:
#             resp = 'REGULAR'
#         dicionario['situação'] = resp
#     return dicionario
#
# print(notas(5.5, 9.5, 10, 6.5, sit=True))
# help(notas)

# 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.
""" Minha solução:
def escreva(texto, cor=45):
    print(f'\033[0:{cor}m ', end='')
    print('~'*(len(texto) + 4))
    print(f' {texto}')
    print('~'*(len(texto) + 4))
    print(f'\033[m')
def helpFunc(func):
    print('help: ', help(func))
    return f'\033[0:40m{help(func)}\033[m'
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 46)
    func = input('Digite a função ou Biblioteca: ')
    if func.upper() == 'FIM':
        escreva('VOLTE SEMPRE!')
        break
    escreva(f"Acessando o manual do comando '{func}'", 44)
    print(helpFunc(func))

"""
# solução do Guanabara:
c = ('\033[m',          # 0 - sem cores
     '\033[0:30:41m',   # 1 - vermelho
     '\033[0:30:42m',   # 2 - verde
     '\033[0:30:43m',   # 3 - amarelo
     '\033[0:30:44m',   # 4 - azul
     '\033[0:30:45m',   # 5 - roxo
     '\033[0:30:46m',   # 6 -
     '\033[0:30:47m',   # 7 - cinza
     '\033[7m',         # 8 - fundo branco e escrita em preto
     '\033[0:35:40m',   # 8 - fundo branco
)


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[8], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    print(c[cor], end='')
    print('~'*(len(msg) + 4))
    print(f'  {msg}')
    print('~'*(len(msg) + 4))
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 4)
