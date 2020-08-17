# Condições:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro clássico')

# condição simplificada:
print('carro novo' if tempo <= 3 else 'carro clássico')

# aula prática:
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {} !'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média é {:.2f} !'.format(media))
if media >= 6:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
# Simplificada
print('Parabéns!' if media >= 6 else 'Estude mais!')