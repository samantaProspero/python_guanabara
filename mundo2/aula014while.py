# while
"""
enquanto não maça
    passo
pega

while not maça
    passo
pega
Desafios:
"""
# 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""resp = input(" Digite seu sexo [m/f]: ").strip().lower()
while resp not in 'mf':
    print('Digitação incorreta!')
    resp = input(" Digite o sexo [m/f]: ")"""

# 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

"""import random
n1 = random.randint(0, 10)
n2 = int(input('Digite um número inteiro entre 0 e 10: '))
count = 1
while n1 != n2:
    n2 = int(input('Digite um número inteiro entre 0 e 10: '))
    count +=1
if count == 1:
    print('Vocẽ precisou de 1 tentativa para acertar')
else:
    print('Vocẽ precisou de {} tentativas para acertar'.format(count))"""


# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

"""n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
maior = 0
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')

operacao = int(input('>>>> Escolha uma das opções: '))
while operacao != 5:
    if operacao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif operacao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif operacao == 3:
        if n1>n2:
            maior = n1
        elif n2> n1:
            maior = n2
        print('{} é o maior deles'.format(maior))
    elif operacao == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    print('=--'*10, end='')
    print('=')
    operacao = int(input('>>>> Escolha uma das opções: '))
print('VOLTE SEMPRE!')"""

# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

"""num = int(input('Digite um número inteiro: '))
count = 1
fatorial = 1
while count<= num:
    fatorial *= count
    count += 1
print('{}! é {}.'.format(num, fatorial))"""

# 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão P.A.: '))
n = 1
while n<=10:
    an = a1 + (n-1)*r
    print(an, end='->')
    n += 1
print('FIM')"""

# 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

"""a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão P.A.: '))
n = 1
an = 0
while n <= 10:
    an = a1 + (n-1)*r
    print(an, end='->')
    n += 1
print('PAUSE')
total = 10
mais = int(input('Quantos termos mais deseja calcular? '))
while mais != 0:
    count = 1
    while mais >= count:
        an += r
        print(an, end='->')
        count += 1
        total += 1
    print('PAUSE')
    mais = int(input('Quantos termos mais deseja calcular? '))
print('a progressão foi terminada com {} termos mostrados'.format(total))"""


# 063: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""print('-'*30)
print('\033[1:35mSequência de Fibonacci\033[m')
print('-'*30)
n = int(input('Digite a quantidade de termos desejados: '))
t1 = 0
t2 = 1
print('\033[1:35m~\033[m'*30)
print('{} -> {}'.format(t1, t2), end=' -> ')
count = 2
while count < n:
    tn = t1 + t2
    print(tn, end=' -> ')
    t1 = t2
    t2 = tn
    count += 1
print('FIM')
print('\033[1:35m~\033[m'*30)"""

# 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""count = soma = 0
num = int(input('Digite um número inteiro: '))
while num != 999:
    soma += num
    count += 1
    num = int(input('Digite um número inteiro: '))
print('Foram digitados {} números cuja soma é {}'.format(count, soma))"""

# 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = str(input('Digite vários números inteiros separados por vírgula: ')).strip()
lista = num.split(',')
soma = count = maior = menor = 0
while count < len(lista):
    valor = int(lista[count])
    soma += valor
    if count == 0:
        menor = valor
        maior = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    count += 1
    resp = str(input('Quer continuar? [s/n]: ')).lower()
    while resp == 's':
        numero = int(input('Digite um número inteiro: '))
        sum += numero
        count += 1
        if numero > maior:
            maior = valor
        elif numero < menor:
            menor = valor
    resp = str(input('Quer continuar? [s/n]: ')).lower()
print('A média dos {} números é {}, sendo {} o maior número e {} é o menor deles'.format(soma/(count + 1), count + 1, maior, menor))
