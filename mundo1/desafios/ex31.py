# Desenvolva um programa que pergunta a distância de uma viagem em km
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
# R$ 0,45 por km para viagens acima de 200km

distancia = int(input('Digite a distância da viagem em kilômetros: '))
if distancia <= 200:
    print('A viagem custará R$ {}!'.format(distancia*0.5))
else:
    print('A viagem custará R$ {}!'.format(distancia*0.45))