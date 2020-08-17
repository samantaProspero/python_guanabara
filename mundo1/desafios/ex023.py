# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
numero = input("Digite um número entre 0 e 9999: ")

print('unidade: ', numero[-1])
print('dezena: ', numero[-2])
print('centena: ', numero[-3])
print('milhar: ', numero[-4])