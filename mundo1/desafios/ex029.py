# escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = int(input('Digite a velocidade: '))
if velocidade >80:
    multa = (velocidade - 80)*7
    print('Vocẽ foi multado no valor de R$ {}!'.format(multa))
else:
    print('Parabéns, continue respeitando os limites de velocidade.')