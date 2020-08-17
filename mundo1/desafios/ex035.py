# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input("Digite a medida do primeiro segmento: "))
r2 = float(input("Digite a medida do segundo segmento: "))
r3 = float(input("Digite a medida do terceiro segmento: "))

if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
    print("Os três segmentos podem formar um triângulo!")
else:
   print("Os três segmentos não podem formar um triângulo!")