# Escreva um programa que:
# Faça o computador pensar em um múmero inteiro entre 0 e 5,
# e peça para o usuário tentar adivinhar o número
# O programa deverá dizer na tela se o usuário venceu ou perdeu.

import random
from time import sleep
n1 = random.randint(0,5)
n2 = int(input('Digite um número inteiro entre 0 e 5: '))
print('PROCESSANDO ....')
sleep(3)
if n1 == n2:
    print('Parabéns, você venceu')
else:
    print('Vocẽ perdeu, o número seria {}, não {}'.format(n1, n2))

