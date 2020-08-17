"""
laços de repetição: for

for c in range(1,10):
    passo
pega

for count in range(1, 6):
    print('Oi')
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for count in range(i, f+1, p):
    print(count)
print('FIM')
"""
# 11 desafios

# 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
for count in range(10, 0, -1):
    print(count)
    sleep(1)
print('ZERO....')
"""
# 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
for number in range(2, 51, 2):
    print(number, end=' ')
print('')
"""
# 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
"""
sum = 0
count=0
for number in range(3, 501, 3):
    sum += number
    count += 1
print('A soma dos {} vale {}'.format(count, sum))
"""
# 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
"""
num = int(input('Digite um número inteiro: '))
print('Tabuada do {}: '.format(num))
for count in range (1, 11):
    print('{} x {:2} = {}'.format(num, count, num * count))
"""
# 050: Desenvolva um programa que
# leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
"""
sum = 0
for count in range( 1, 7):
    num = int(input('Digite o {} número inteiro: '.format(count)))
    if num % 2 == 0:
        sum += num
print('A soma dos números pares digitados é {}'.format(sum))
"""
# 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
"""
a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão P.A.: '))
for n in range(a1, (a1 + 9*r)+r, r):
    print(n, end='->')
print('FIM')
"""
# 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input('Digite um número inteiro: '))
verificador = 0
for count in range(2, int(num/2)):
    if num%count==0:
        verificador = 1
if verificador == 0:
    print('O número {} é primo'.format(num))
else:
     print('O número {} não é primo'.format(num))
"""

# 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# solução 1
"""frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += str(junto[letra])
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')"""

#solução 2
"""
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
"""
# 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""from datetime import date
count=0
for n in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(n)))
    if date.today().year - ano >= 21:
        count += 1
print('{} pessoas atingiram a maioridade e {} não atingiram'.format(count, 7-count))"""

# 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""menor = 1000
maior = 0
for n in range(1,6):
    peso = int(input('Digite um peso: '))
    if  peso <= menor:
        menor = peso
    if peso >= maior:
        maior = peso
print('O maior peso é {}, enquanto {} é o menor deles'.format(maior, menor))
"""
# 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

sum = 0
mulheres = 0
homem= 0
nomeHomem=''
count = 0
for pessoa in range(1, 5):
    count += 1
    print("{} {}ª PESSOA {}".format('-'*3, count, '-'*3))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sum += idade
    if sexo in 'Ff':
        if idade < 20 :
            mulheres +=1
    elif sexo in 'Mm':
        if idade > homem:
            homem = idade
            nomeHomem = nome
print('A média das idades é: {}'.format(sum/count))
print('O homem mais velho é o: {}'.format(nomeHomem))
print('O total de mulheres com menos de vinte anos é {}.'.format(mulheres))


