# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = (input("Digite seu nome completo: ")).strip()
possui = nome.lower()
print("silva" in possui)