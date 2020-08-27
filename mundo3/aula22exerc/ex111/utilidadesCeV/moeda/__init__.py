def dobro(n):
    return n*2


def metade(n):
    return n/2


def moeda(n):
    return f'R$ {n:.2f}'.replace('.', ',')


def aumentar(a, x):
    return (1 + x/100)*a


def diminuir(a, x):
    return (1 - x/100)*a


def resumo(n, aum, red):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{aum}% de aumento: \t{moeda(aumentar(n, aum))}')
    print(f'{red}% de redução: \t{moeda(diminuir(n, red))}')
    print('-'*30)
