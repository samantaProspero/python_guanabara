"""
listas compostas

"""
# 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
"""
lista = []
dado = []
while True:
    dado.append(input('Digite um nome: '))
    dado.append(float(input('Digite um peso: ')))
    if len(lista) == 0:
        maior = dado[1]
        menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar[s, n]: ')).strip().lower()[0]
    if resp == 'n':
        break
print('-'*20)

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi: {maior}Kg de ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi: {menor}Kg de ', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print('\n')
print('-'*20)
"""
# 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n+1}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('-'*20)
print(f'Os números pares são {lista[0]}, enquanto os ímpares são {lista[1]}.')
print('-'*20)
"""
# 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = (int(input(f'Digite o termo [{i},{j}] da matriz: ')))
print('-'*25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-'*25)
"""
# 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
'''
minha solução:
matriz = []
temp = []
soma = 0
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input('Digite o termo da matriz: '))
        temp.append(num)
        soma += num
    matriz.append(temp[:])
    temp.clear()
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-'*20)
print(f'A soma dos valores digitados vale: {soma}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'A soma dos valores da segunda linha é: {matriz[1][0] + matriz[1][1] + matriz[1][2]}')
'''
# Outra solução:
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = (int(input(f'Digite o termo [{i},{j}] da matriz: ')))

print('-'*25)
soma = somac = 0
maior = matriz[1][0]
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            somac += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    print()
print('-'*25)
print(f'A soma dos valores pares digitados vale: {soma}')
print(f'A soma dos valores da terceira coluna é: {somac}')
print(f'O maior valor da segunda linha é: {maior}')
print('-'*25)
"""
# 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista = []
jogo = []
quant = int(input('Digite a quantidade de jogos que deseja gerar: '))
for n in range(0, quant):
    for i in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.sort()
        jogo.append(num)
    lista.append(jogo[:])
    jogo.clear()
    print(f'{n + 1}º jogo: {lista[n]}')
    sleep(1)
"""
#089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
nome = []
nota = []
media = []
aluno = []
lista = []
while True:
    nome.append(str(input('Digite o nome: ')).strip())
    nota.append(float(input('Digite a primeira nota: ')))
    nota.append(float(input('Digite a segunda nota: ')))
    media.append((nota[0] + nota[1]) / 2)
    aluno.append(nome[:])
    aluno.append(nota[:])
    aluno.append(media[:])
    lista.append(aluno[:])
    nota.clear()
    nome.clear()
    media.clear()
    aluno.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
print('-'*30)
print('Nº', end=' ')
print('NOME', end=' ')
print('MEDIA')
print('-'*30)

for pos, n in enumerate(lista):
    print(f'{pos} {n[0]} {n[2]}')
result = int(input('Digite o número do aluno do qual deseja verificar as notas: '))
print(f'Notas: {lista[result][1]}')
"""
# outra forma
"""
lista = []
while True:
    nome = (str(input('Digite o nome: ')).strip())
    nota1 = (float(input('Digite a primeira nota: ')))
    nota2 = (float(input('Digite a segunda nota: ')))
    media = ((nota1 + nota2) / 2)
    lista.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
print('-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)

for pos, n in enumerate(lista):
    print(f'{pos:<4}{n[0]:<10}{n[2]:>8.1f}')
result = 0

while True:
    print('-'*30)
    result = int(input('Digite o número do aluno do qual deseja verificar as notas [999 para parar]: '))
    if result == 999:
        print('Finalizando ...')
        break
    if result <= len(lista) - 1:
        print(f'Notas de {lista[result][0]}: {lista[result][1]}')
print('<<< Volte Sempre! >>>')


retorno:
------------------------------
Nº  NOME         MÉDIA
------------------------------
0   Ana            8.0
1   Samanta        6.5
2   Carlos        10.0
"""