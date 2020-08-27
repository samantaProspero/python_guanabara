
# 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda
num = float(input('Digite um número: '))

print(f'Aumentando 10% temos: {moeda.aumentar(num)}')
print(f'Reduzindo 13% temos: {moeda.diminuir(num)}')
print(f'O dobro de {num} é: {moeda.dobro(num)}')
print(f'A metade de {num} é: {moeda.metade(num)}')
"""
# 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
"""import moeda
num = float(input('Digite um número: '))

print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumentar(num))}')
print(f'Reduzindo 13% temos: {moeda.moeda(moeda.diminuir(num))}')
print(f'O dobro de {num} é: {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {num} é: {moeda.moeda(moeda.metade(num))}')
print(f'O número {num} formatado para moeda fica: {moeda.moeda(num)}')
"""
# 109: Modifique as funções que foram criadas no desafio 107 para que
# elas aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda
num = 27.456
resp = True
print(f'Aumentando 10% temos: {moeda.aumentar2(num, resp)}')
print(f'Reduzindo 13% temos: {moeda.diminuir2(num, resp)}')
print(f'O dobro de {num} é: {moeda.dobro2(num, resp)}')
print(f'A metade de {num} é: {moeda.metade2(num, resp)}')
"""
# 110: Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui.
"""
import moeda

num = float(input('Digite um valor em reais: R$ '))
aum = float(input('Digite a porcentagem do aumento: '))
red = float(input('Digite a porcentagem de redução: '))
print(moeda.resumo(num, aum, red))
"""

