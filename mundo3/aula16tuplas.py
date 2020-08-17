"""
Variaveis compostas :
- Tuplas () os () não são obrigatórios
- listas []
- dicionarios {}

TUPLAS são imutaveis

primeira forma:
for comida in lanche:
    print(f'Eu vou comer {comida}')
segunda forma
for count in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[count]}')

terceira forma
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# imprime em ordem alfabética: ['Hamburguer', 'Pizza', 'Pudim', 'Suco']
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
# a + b é (2, 5, 4, 5, 8, 1, 2)
c = b + a

# c = (5, 8, 1, 2, 2, 5, 4)
print(c)
# conta quantas vezes aparece o 2 em c
print(c.count(2))
# Indicar o indice do número 2
print(c.index(2))
# Indicar o indice do número 2 a partir da posição 4
print(c.index(2, 4))

pessoa = ('Gustavo', 39, 'M', 99.88)
# pode deletar a tupla inteira mas não dá pra deletar parte dela
# apaga tupla: equivalente a del(pessoa)
del pessoa
"""

# DESAFIOS:
# 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

"""lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'deznove', 'vinte')
num = int(input('Digite um inteiro entre 0 e 20: '))
print(f'Você digitou o número {lista[num]}.')"""

# 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#  na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

"""campeonato = ('Atlético-MG',' Athletico-PR', 'Internacional', 'Grêmio', 'Atlético-GO', 'Vasco', 'Bahia', 'São Paulo', 'Sport', 'Flamengo', 'Bragantino', 'Palmeiras', 'Botafogo', 'Corinthians', 'Goiás', 'Fluminense', 'Santos', 'Ceará', 'Fortaleza', 'Coritiba')
print('='*30)

print('a) Os cinco primeiros colocados são: ')
for index in range(0, 5):
    print(f'{index +1}º colocado: {campeonato[index]}')

print('='*30)

print('b) Os 4 últimos colocados são: ')
for index in range(-4, 0):
    print(f'{20 + (index +1)}º colocado: {campeonato[index]}')

print('='*30)
print(f'c) Times em ordem alfabética: {sorted(campeonato)}')
print('='*30)
print(f'd) Vasco está no indice: {campeonato.index("Vasco")}')"""

# 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""from random import randint

lista = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
menor = maior = 0
for index in range(0, 5):
    if index == 0 or lista[index] < menor:
        menor = lista[index]
    if index == 0 or lista[index] > maior:
        maior = lista[index]
print('=' * 30)
print(lista)
print('=' * 30)
print(f'O menor número é: {menor}.')
print(f'O maior número é: {maior}.')
print('=' * 30)"""

# 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#  077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
