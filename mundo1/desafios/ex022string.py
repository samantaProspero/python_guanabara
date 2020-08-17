# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras tem ao todo sem contar espaços;
# Quantas letras tem no primeiro nome;

nome= input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
espacos=(nome.count(' '))
print('Seu nome possui {} caracteres'.format(len(nome)))
print('Seu nome possui {} letras'.format(len(nome) - espacos))
separado = nome.split()
primeira = separado[0]
print('Seu primeiro nome possui {} letras'.format(len(primeira)))
