# Crie um programa que leia um número real qualquer pelo teclado, e mostre sua parte inteira
from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira do número {} é {}'.format(num, trunc(num)))
#ou:
print('A parte inteira do número {} é {}'.format(num, int(num)))