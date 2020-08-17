# Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00 => aumento de 10%
# Para salários inferiores ou iguais a R$1250,00 => aumento de 15%

salario = float(input("Digite o valor do seu salário atual: "))
if salario>1250:
    print('Seu novo salário será de: R$ {:.2f}'.format(salario*1.1))
else:
    print('Seu novo salário será de: R$ {:.2f}'.format(salario*1.15))
