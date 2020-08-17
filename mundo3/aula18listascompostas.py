"""
listas compostas

"""
# 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

"""lista = []
dado = []
while True:
    for c in lista:
        dado.append(input('Digite um nome: '))
        dado.append(int(input('Digite um peso: ')))
        lista.append(dado[:])
        dado.clear()
        if c == 0:
            maior = c
            menor = c
        elif c[1] > maior:
            maior = c
        elif c[1] < menor:
            menor = c
        resp = ' '
        while resp not in 'sn':
            resp = str(input('Deseja continuar[s, n]: ')).strip().lower()[0]
        if resp == 'n':
            break
print('-'*20)
print(f'Foram cadastradas {len(lista)} pessoas.')
print('-'*20)"""

# 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = []
pares = []
impares = []
for n in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
lista.append(pares)
impares.sort()
lista.append(impares)
print('-'*20)
print(f'Os número pares são {lista[0]}, enquanto os ímpares são {lista[1]}.')
print('-'*20)"""

# 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.



# 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

"""from random import randint
lista = []
jogo = []
quant = int(input('Digite a quantidade de jogos que deseja gerar: '))
for n in range(0, quant):
    for i in range(0, 6):
        jogo.append(randint(1, 60))
    lista.append(jogo[:])
    jogo.clear()
print(f'Sua lista de jogos: \n{lista}')"""

#089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

"""nota = []
lista = []
while True:
    nota.append(str(input('Digite o nome: ')).strip())
    nota.append(float(input('Digite a primeira nota: ')))
    nota.append(float(input('Digite a segunda nota: ')))
    lista.append(nota[:])
    nota.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar[sn]: ')).strip().lower()[0]
    if resp == 'n':
        break
for n in lista:
    print(f'Nome: {n[0]}, notas: {n[1]} e {n[2]}, média: {(n[1] + n[2]) * 0.5}')"""
