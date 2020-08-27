# 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos
# chamados moeda e dado. Transfira todas as funções utilizadas nos
# desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
from utilidadesCeV import moeda

num = float(input('Digite um valor em reais: R$ '))
aum = float(input('Digite a porcentagem do aumento: '))
red = float(input('Digite a porcentagem de redução: '))
print(moeda.resumo(num, aum, red))
"""
# 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como
# a função input(), mas com uma validação de dado para aceitar apenas valores
# que seja monetários.

from utilidadesCeV import moeda, dado

num = dado.leiaDinheiro('Digite o preço: R$ ')
print(moeda.resumo(num, 35, 22))
