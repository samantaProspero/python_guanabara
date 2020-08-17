# Faça um programa que leia um ano qualquer e mostre se é bissexto
from datetime import date
ano = int(input("Que ano quer analisar/ Digite zero para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano%100 == 0:
    if ano%400 == 0:
        print('O ano {} é ano bissexto!'.format(ano))
    else:
        print('O ano {} não é ano bissexto!'.format(ano))
else:
    if ano%4 == 0:
        print('O ano {} é ano bissexto!'.format(ano))
    else:
        print('O ano {} não é ano bissexto!'.format(ano))