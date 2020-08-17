# Faça um programa que leia um ângulo qualquer e mostre na tela os valores seno, cosseno e tangente desse angulo
import math
angulo= float(input("Digite a medida de um ângulo: "))
grau= math.radians(angulo)
print("o seno do angulo {} é : {:.2f}".format(angulo, math.sin(grau)))
print("o cosseno do angulo {} é : {:.2f}".format(angulo, math.cos(grau)))
print("o tangente do angulo {} é : {:.2f}".format(angulo, math.tan(grau)))