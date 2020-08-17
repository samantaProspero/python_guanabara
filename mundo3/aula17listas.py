"""
listas
são mutáveis
lanche = []

ADICIONAR
lanche.append('pudim') - adiciona no final
lanche.insert(0,'pão') - insere item páo no índice zero e o que estava no zero vai para o indice 1

REMOVER
del lanche -deleta lista
del lanche[3] ou lanche.pop(3) - deleta item da lista,
                                   pop sem indice: deleta o último item
                                   pop com índice: deleta o item do indice indicado
lanche.remove('pizza') - deleta item pelo seu valor, não pelo indice, somente o prinmeiro encontrado
(em todos os casos ele elimina o elemento e rearruma a lista)

CRIAÇÃO
valores = list(range(4,11))
retorno: [4, 5, 6, 7, 8, 9, 10]

METODOS
valores.sort()
valores.sort(reverse= True) - ordena de forma decrescente
len(valores)

num = [2, 5, 9, 1]
num[2] = 3
retorno: num = [2, 5, 3, 1]
num[4] = 7 dá erro pois não existe indice 4
para inserir:
num.append(7)
retorno: num = [2, 5, 3, 1, 7]
num.insert(2,0)
retorno: num = [2, 5, 0, 3, 1]

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!)

a = [2, 3, 4, 7]
b = a
a e b são iguais
b[2] = 8 - muda nas duas listas
para b não ter ligação com a, e ser apenas uma cópia de a:
b = a[:]
b[2] = 8 - muda só no b

"""
# 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print('-'*40)
print(f'Vocẽ digitou os valores: {valores}')
print('-'*40)
maior = max(valores)
menor = min(valores)
print(f'O maior valor é {maior} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == maior:
       print(c + 1, end=' ')
print(f'\nO menor valor é {menor} nas posições: ', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(c + 1, end=' ')

print(f'\n{"-"*18} fim {"-"*18}')"""

# 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

"""valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor já existe, não pode ser adicionado')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso')
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
    if resp in 'n':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')"""

# 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

"""lista = list()
for c in range(0, 5):
    num = int(input('Digite um número inteiro: '))
    if c == 0 or num > lista[- 1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)"""

# 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

"""valores = list()
count = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
    if resp in 'n':
        break
print('-'*40)
print(f'a) Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'b) Os valores digitados foram:\n {valores}')
if 5 in valores:
    print('c) O valor 5 está na lista')
else:
    print('c) O valor 5 não está na lista')
print('-'*40)"""

# 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

"""valores = list()
pares = list()
impares = list()

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
    if resp in 'n':
        break
print(f'Os números digitados foram: {valores}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')"""

# 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


# exp = str(input('Digite uma expressão Matemática: ')).strip()
# while True:


