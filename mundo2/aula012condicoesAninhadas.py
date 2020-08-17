'''
if:
    bloco
elif:
    bloco
else:
    bloco
'''
# 10 desafios 036 em diante:


# 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

'''
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
tempo = int(input('Em quantos a casa será quitada? '))
prestacao = casa/tempo/12
if prestacao>salario*0.3:
    print('Sálario insuficiente para este financiamento')
else:
    print('O financiamento está aprovado e a prestações mensais serão de R$ {:.2f}'.format(prestacao))
'''

# 037 Escreva um programa que leia um número inteiro e
# peça para o usuário escolher qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# numero = int(input('Digite o valor de um número inteiro: '))
# print('''Informações sobre a base de conversão:
# [ 1 ] para binário
# [ 2 ] para octal
# [ 3 ] para hexadecimal''')
# base = int(input('Digite a base de conversão: '))
# if base == 1:
#     print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
# elif base ==2:
#     print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
# elif base ==3:
#     print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
# else:
#     print('Base de conversão incorreta')


# 038 Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# O primeiro valor é maior.
# O segundo valor é maior.
# não existe valor maior, os dois são iguais.
'''
n1 = int(input('Digite o valor de um número inteiro: '))
n2 = int(input('Digite o valor de um segundo número inteiro: '))

if n1>n2:
    print('O primeiro valor é maior')

elif n2>n1:
    print('O primeiro valor é maior')
else:
    print('não existe valor maior, os dois são iguais.')
'''

# 039 Faça um programa que leia o ano de nascimento de um jovem, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar no serviço militar
# Se já passou o tempo do alistamento no serviço militar
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
if idade < 17:
    print('Você ainda vai se alistar, faltam {} anos!'.format(17-idade))
elif idade == 17:
    print('Você deve se alistar ainda neste ano')
else:
    print('Já passou um período de {} anos do seu período de alistamento'.format(idade -17))
'''

# 040 crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagemm no final:
# média abaixo de 5.0: REPROVADO
# média entre 5.0 e 6.9: RECUPERAÇÃO
# média 7.0 ou superior: APROVADO

'''
n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))
media = (n1 + n2)/2

if media < 5.0:
    print('média abaixo de 5.0: REPROVADO')

elif media >= 7.0:
    print('média 7.0 ou superior: APROVADO')
else:
    print('média entre 5.0 e 6.9: RECUPERAÇÃO')
'''
# 041 A Confederação Nacional de Natação precisa de um programa que:
# leia o ano de nascimento do atleta e mostre sua categoria, de acordo com a idade::
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SÊNIOR
# acima: MASTER
'''
from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} e está na categoria \033[36mMIRIM\033[m!'.format(idade))
elif idade <= 14:
    print('Você tem {} e está na categoria \033[36mINFANTIL\033[m!'.format(idade))
elif idade <= 19:
    print('Você tem {} e está na categoria \033[36mJUNIOR\033[m!'.format(idade))
elif idade <= 20:
    print('Você tem {} e está na categoria \033[36mSÊNIOR\033[m!'.format(idade))
else:
    print('Você tem {} e está na categoria \033[36mMASTER\033[m!'.format(idade))
'''

# 042  Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar:
# que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais
# Isósceles: dois lados são iguais
# Escaleno: os três lados são diferentes

'''
r1 = float(input("Digite a medida do primeiro segmento: "))
r2 = float(input("Digite a medida do segundo segmento: "))
r3 = float(input("Digite a medida do terceiro segmento: "))


if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
    if r1 != r2 and r2 != r3 and r1 != r3:
        print("Os três segmentos podem formar um triângulo escaleno!")
    elif r1 != r2 or r2 != r3 or r1 != r3:
        print("Os três segmentos podem formar um triângulo isósceles!")
    else:
        print("Os três segmentos podem formar um triângulo equilátero!")
else:
   print("Os três segmentos não podem formar um triângulo!")
'''
# 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo co a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
'''
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/ altura**2

if imc <= 18.5:
    print('Você tem imc: {:.1f} está \033[33m abaixo do peso\033[m!'.format(imc))
elif imc <= 25:
    print('Você tem imc: {:.1f} está com \033[32m peso ideal\033[m!'.format(imc))
elif imc <= 30:
    print('Você tem imc: {:.1f} está com \033[33ma sobrepeso\033[m!'.format(imc))
elif imc <= 40:
    print('Você tem imc: {:.1f} está com \033[33m obesidade\033[m!'.format(imc))
else:
    print('Você tem imc: {:.1f} está com \033[31m obesidade mórbida\033[m!'.format(imc))
'''
# 044 Elabore um programa que calcule o valor a ser pago por um produto, considerando:
# seu preço normal e a condição de pagamento:
# à vista (dinheiro/cheque): 10% de desconto
# à vista (cartão): 5% de desconto
# em até duas vezes no cartão: preço normal
# em três vezes ou mais no cartão: 20% de juros

# preco = float(input('Digite o valor normal do produto: '))
# print('''Informações sobre a condições de pagamento:
# [ 1 ] à vista (dinheiro/cheque);
# [ 2 ] à vista (cartão);
# [ 3 ] em até duas vezes no cartão
# [ 4 ] em três vezes ou mais no cartão''')
# condicao = int(input('Digite o numero correspondente à forma de pagamento: '))
# if condicao == 1:
#     valor = preco*0.90
# elif condicao == 2:
#     valor = preco*0.95
# elif condicao == 3:
#     valor = preco
# else:
#     valor = preco*1.2
# print('O produto custará R$\033[35m {:.2f}\033[m!'.format(valor))

# 045 Crie um programa que faça o computador jogar Jokenpô com você.

# minha resolução:
# from random import randint
# print('''Informações sobre a jogada:
# [ 1 ] pedra;
# [ 2 ] papel;
# [ 3 ] tesoura ''')
# maq = randint(1, 3)
# jogada = int(input('Digite o numero correspondente à sua jogada: '))
# if maq == jogada:
#     print('Deu empate!')
# elif maq == 1:
#     if jogada == 2:
#         print('Você ganhou! Eu joguei pedra!')
#     else:
#         print('Você perdeu! Eu joguei pedra!')
# elif maq == 2:
#     if jogada == 3:
#         print('Você ganhou! Eu joguei papel!')
#     else:
#         print('Você perdeu! Eu joguei papel!')
# elif maq == 3:
#     if jogada == 1:
#         print('Você ganhou! Eu joguei tesoura!')
#     else:
#         print('Você perdeu! Eu joguei tesoura!')

#resolução do Guanabara:

from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] pedra;
[ 1 ] papel;
[ 2 ] tesoura ''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)

if computador == jogador:
    print('EMPATE!')
elif computador == 0:
    if jogador == 1:
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
elif computador == 1:
    if jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
