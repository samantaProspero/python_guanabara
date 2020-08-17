# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O primeiro e o último nome separadamente;
nome = input('Digite seu nome completo: ')
separado = nome.split()
print('Seu primeiro nome é: {}'.format(separado[0]))
print('Seu último nome é: {}'.format(separado[-1]))