""""
FUNÇÕES:

def mostraLinha():
    print('-'*20)

def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem('SISTEMA DE ALUNOS')

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(4,5)
soma(b=5, a=4)

# O * significa desempacotar, ié,
# independente da quantidade de parâmetros enviados, o programa deve joga-los dentro de num:

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
# o contador criou uma tupla para cada chamada
# retorno:
# Recebi os valores (2, 1, 7) e são ao todo 3 números
# Recebi os valores (8, 0) e são ao todo 2 números
# Recebi os valores (4, 4, 7, 6, 2) e são ao todo 5 números

# para trabalhar com listas ao invés de tuplas:
valores = [7, 2, 5, 0, 4]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
dobra(valores)
print(valores)

def somatorio(*valores):
    s = 0;
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

somatorio(5, 2)
somatorio(2, 9, 4)
"""
# 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e
# mostre a área do terreno.
"""
medida1 = float(input("Digite a primeira medida do terreno: "))
medida2 = float(input("Digite a segunda medida do terreno: "))
def area(a, b):
    print(f'A área do terreno com dimensões {a} x {b} mede {a*b} metros quadrados.')
area(medida1, medida2)
"""
# 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

"""
def escreva(texto):
    print('~'*(len(texto) + 4))
    print(f'  {texto}')
    print('~'*(len(texto) + 4))


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
"""
# 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

"""from time import sleep


def mostraLinha():
    print('-'*30)


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if passo > 0:
        fim += 1
    elif passo == 0 and fim <= inicio:
        passo = -1
        fim -= 1
    elif passo == 0 and fim > inicio:
        passo = 1
        fim += 1
    else:
        fim -= 1
    for n in range(inicio, fim, passo):
        sleep(0.1)
        print(n, end=' ')
    print('FIM!')


mostraLinha()
contador(1, 10, 1)
mostraLinha()
contador(10, 0, -2)
mostraLinha()
print('Agora é a sua vez de personalizar a contagem: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
mostraLinha()

contador(inicio, fim, passo)"""


# 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que
# analisar todos os valores e dizer qual deles é o maior.

"""from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    sleep(0.5)
    if len(num) > 0:
        maximo = max(num)
    else:
        maximo = 0
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo. ')
    print(f'O maior valor informado foi {maximo}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
"""
# 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
numeros = []


def sorteia(numeros):
    print('Sorteando os 5 valores da lista:', end=' ')
    for n in range(0, 5):
        num = randint(1, 50)
        numeros.append(num)
        print(num, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lst}, temos {soma}.')


sorteia(numeros)
somaPar(numeros)
