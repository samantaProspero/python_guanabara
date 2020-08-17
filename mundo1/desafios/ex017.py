# Faça um programa que leia os catetos de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cat1 = float(input('Digite a medida do cateto oposto: '))
cat2 = float(input('Digite a medida do cateto adjacente: '))
hip = math.hypot(cat1, cat2)
#ou
hipotenusa = math.pow(cat1, 2) + math.pow(cat2, 2)
print("math.hypot: ", hip)
print('Dados os catetos {} e {}, a medida da hipotenusa é: {}'.format(cat1, cat2, math.sqrt(hipotenusa)))