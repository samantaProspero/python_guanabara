def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return a


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[0:032m{c} - \033[034m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc
