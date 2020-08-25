"""
Dicionários
possui indices literais

tuplas ()
listas []
dicionarios {}

dados = disc() ou dados = {}
dados = { 'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

append não funciona,
dados['sexo'] = 'M' vai criar a casa e colocar a str M dentro
del dados['idade']

filme ={
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

# retorno:
# dict_values(['Star Wars', 1977, 'George Lucas'])
# dict_keys(['titulo', 'ano', 'diretor'])
# dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

filme['ano'] = 1976
filme['decada'] = 'oitenta' (insere a chave década e seu valor)(substitui o append)

for k,v in filme.items():
    print(f'O {k} é {v}')
# retorno:
# O titulo é Star Wars
# O ano é 1977
# O diretor é George Lucas

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1.copy())  (.copy equivale ao [:] das listas)
brasil.append(estado2)

print(brasil)
# [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0])
# {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[0]['uf'])
# Rio de Janeiro

outro exemplo:
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
# retorno:
# São Paulo SP
# Rio de Janeiro RJ
# Ceará CE
"""
# Desafios:
# 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
"""aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}:  '))
print(aluno['media'])
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'

elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Nome é igual a: {aluno["nome"]}')
print(f'Média é igual a: {aluno["media"]}')
print(f'Situação é igual a: {aluno["situacao"]}')
"""
# 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

"""from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
rancking = list()
print('Valores sorteados:')
for k, v in jogadas.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('Ranking dos jogadores: ')
rancking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rancking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
"""
# 092:Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o(com idade) em um dicionário
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
cadastro = dict()
cadastro['name'] = str(input('Digite seu nome: ')).strip()
cadastro['idade'] = date.today().year - int(input('Digite seu ano de nascimento: '))
cadastro['ctps'] = int(input('Digite o número de sua CTPS: [0 caso não tenha]: '))
if cadastro['ctps'] != 0:
    contratacao = int(input('Digite o ano da contratação: '))
    cadastro['contratacao'] = contratacao
    salario = float(input('Digite seu salário: '))
    cadastro['salario'] = salario
    aposenta = cadastro['idade'] + 35 - (date.today().year - cadastro['contratacao'])
print(f'nome: {cadastro["name"]}.')
print(f'Você tem {cadastro["idade"]} anos. ')
print(f'CTPS de numero {cadastro["ctps"]}. ')
if cadastro['ctps'] != 0:
    print(f'E irá se aposentar com {aposenta} anos')
    """
# 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

"""
jogador = {}
jogador['nome'] = str(input('Digite o nome do jogador: ')).strip()
partidas = int(input('Digite o número de partidas jogadas:'))
gols = []

for i in range(0, partidas):
    gols.append(int(input(f'Gols na {i + 1}ª partida: ')))
jogador['gols'] = gols
jogador['soma'] = sum(gols)
print('-'*30)
print(jogador)
print('-'*30)
print(f'O jogador {jogador["nome"]}, jogou {partidas} partidas.')
for i in range(0, len(jogador['gols'])):
    print(f' => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["soma"]} gols.')
print('-'*30)"""
# 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
"""
pessoa = {}
lista = []
soma = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo:[m/f] ')).strip().lower()[0]
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    resp = ' '
    print('-'*30)
    while resp not in 'sn':
        resp = str(input(f'Deseja continuar?[s/n] ')).strip().lower()[0]
    if resp == 'n':
        break
    print('-' * 30)
media = soma/len(lista)
print('-' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'a média de idade é de {media:.2f} anos.')
print('lista de mulheres: ', end=' ')
for i in range(0 , len(lista)):
    if lista[i]['sexo'] =='f':
        print(f'[{lista[i]["nome"]}]', end=' ')
print()
print('Pessoas com idade acima da média: ', end=' ')
for i in range(0, len(lista)):
    if lista[i]['idade'] > media:
        print(f'[{lista[i]["nome"]}]', end=' ')
print()
print('-' * 30)
"""
# 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
gols = []
lista = []
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: ')).strip()
    partidas = int(input('Digite o número de partidas jogadas:'))
    for i in range(0, partidas):
        gols.append(int(input(f'Gols na {i + 1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['soma'] = sum(gols)
    gols.clear()
    lista.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        break
print('-'*30)
print(f'{"cod":<3}  {"nome":<8} {"gols":<15} total')
for i, v in enumerate(lista):
    print(f'{str(i):>3}  {str(v["nome"]):<8} {str(v["gols"]):<15} {v["soma"]}')
print('-'*30)
jog = ' '
while True:
    jog = int(input('Mostrar dados de qual jogador? [999 pra parar] '))
    if jog == 999:
        break
    if jog < 0 or jog > len(lista):
        print(f'Erro! Não existe jogador com o código {jog}')
    else:
        print(f'levantamento do jogador: {jogador["nome"]}')
        for i in range(0, len(lista[jog]['gols'])):
            print(f' => Na partida {i+1}, fez {lista[jog]["gols"][i]} gols.')
print('VOLTE SEMPRE!')
print('-'*30)
