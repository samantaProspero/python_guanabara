"""
while true:
    bloco
    break
"""

# 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

"""n = s = count = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    count += 1
    s += n
print('-'*12)
print(f'A soma dos {count} números inteiros vale: {s}')
print('-'*12)"""

# 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

"""while True:
    n = int(input('Digite um número inteiro [negativo para parar]: '))
    if n <0:
        break
    print('-'*12)
    for p in range(1, 11):
        print(f'{n} x {p:2} = {n*p}')
    print('-'*12)
print('Tabuada finalizada')"""


# 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""from random import  randint
v = 0
while True:
    print('-' * 12)
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'pi':
        tipo = str(input('Par ou ímpar? [p/i] ')).strip().lower()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('-'*12)
    if tipo == 'p':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'i':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break

    print('Vamos jogar novamente ...')

print(f'Você venceu {v} vezes!')"""

# 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

"""maior = mulher = homem = 0
while True:
    print('-'*12)
    idade = int(input('Digite uma idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('Digite o sexo [m/f]: ').lower()
    print('-'*12)
    if sexo == 'm':
        homem += 1
    elif sexo == 'f' and idade < 20:
        mulher += 1
    if idade > 18:
        maior += 1
    resp = ' '
    while resp not in 'yn':
        resp = input('Deseja continuar? [y/n] ').lower()
    if resp == 'n':
        break
print('~'*12)
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulher} mulheres tem menos de 20 anos.')"""

# 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

"""total = caro = barato = count = 0
while True:
    print('-'*12)
    nome = input('Digite o nome do produto: ').lower()
    preco = float(input('Digite o valor: R$ '))
    print('-'*12)
    count += 1
    total += preco
    if preco > 1000:
        caro += 1
    if count == 1 or preco < barato:
        barato = preco
        baratoNome = nome
    resp = ' '
    while resp not in 'yn':
        resp = input('Deseja continuar? [y/n] ').strip().lower()[0]
    if resp == 'n':
        break
print('~'*12)
print(f'Total gasto na compra: {total:.2f}')
print(f'Quantidade de produtos que custaram mais de R$1000,00: {caro}')
print(f'{baratoNome} foi o poduto mais barato e custou R$ {barato:.2f}.')"""

# 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""print('{:^30}'.format('BANCO CEV'))
total = int(input('Digite o valor que você deseja sacar: R$ '))
cinquenta = total//50
vinte = total % 50//20
dez = total % 20//10
um = total % 10
count = cinquenta + vinte + dez + um
print('=' * 18)
print(f'Serão {count} notas:\n{cinquenta} de R$50,00,\n{vinte} de R$ 20,00,\n{dez} de R$ 10,00,\n{um} de R$ 1,00.')
print('=' * 18)"""

