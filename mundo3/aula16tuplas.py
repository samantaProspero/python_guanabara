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
while True:
    num = int(input('Digite um inteiro entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.')
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
print(f'd) Vasco está na {campeonato.index("Vasco") + 1}ª posição.')"""

# 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""from random import randint
lista = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
print('=' * 30)
print(lista)
print('=' * 30)
print(f'O menor número é: {(min(lista))}.')
print(f'O maior número é: {(max(lista))}.')
print('=' * 30)"""

# 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

"""a = int(input('Digite o número: '))
b = int(input('Digite o número: '))
c = int(input('Digite o número: '))
d = int(input('Digite o número: '))

lista = (a, b, c, d)
print(f'Você digitou os valores: {lista}')
count = lista.count(9)
print(f'a) O número 9 apareceu {count} vezes.')

indice = -1
for index, num in enumerate(lista):
    if 3 in lista:
        if num == 3:
            print(f'b) O primeiro valor 3 está na posição {index + 1}.')
    else:
        print(f'b) Não existe número 3 nesta lista.')

    if num % 2 == 0:
        print(f'c) O número {num} é par.')
       par = True"""
# if par != True:
#     print(f'c) Não há números pares nesta lista.')

# 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""listagem = ('lápis', 1.75, 'borracha', 2, 'caderno', 15.90, 'estojo', 25, 'transferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90 )
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-'*40)"""
""" retorno: 
----------------------------------------
           LISTAGEM DE PREÇOS           
----------------------------------------
lápis.........................R$   1.75
borracha......................R$   2.00
caderno.......................R$  15.90
estojo........................R$  25.00
transferidor..................R$   4.20
compasso......................R$   9.99
mochila.......................R$ 120.32
canetas.......................R$  22.30
livro.........................R$  34.90
----------------------------------------
"""
#  077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""lista = ('Crie', 'programa', 'que', 'tenha', 'tupla', 'varias', 'palavras', 'acentos', 'Depois', 'disso', 'mostrar', 'palavra', 'quais', 'vogais')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')"""
""" retorno:
Na palavra Crie temos: i e 
Na palavra programa temos: o a a 
Na palavra que temos: u e 
Na palavra tenha temos: e a 
Na palavra tupla temos: u a 
Na palavra varias temos: a i a 
Na palavra palavras temos: a a a 
Na palavra acentos temos: a e o 
Na palavra Depois temos: e o i 
Na palavra disso temos: i o 
Na palavra mostrar temos: o a 
Na palavra palavra temos: a a a 
Na palavra quais temos: u a i 
Na palavra vogais temos: o a i 
"""
