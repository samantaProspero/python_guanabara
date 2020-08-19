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

# 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

# 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
