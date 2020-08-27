"""
Tratamento de erros e exceções:
Estrutura simples:

try:
    operação
except:
    falhou
else:
    deu certo
finnaly:
    certo/falha

Estrutura mais completa:

try:
    operação
except TypeError:
    falhou
except ValueError:
    falhou
except OSError:
    falhou
else:
    deu certo
finnaly:
    certo/falha


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por zero, Juquinha!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigada!')
"""
# 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

"""
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

def leiaFloat(msg):
    while True:
        try:
            a = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM NÚMERO REAL VÁLIDO!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return a
n = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {real}.')
"""
# 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está disponível no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
"""
# 115a: Vamos criar um menu em Python, usando modularização.

def valida():
    while True:
        try:
            num = int(input('Sua opção: '))
            print('-' * 40)
        except (ValueError, TypeError):
            print(f'\033[0:31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
        else:
            return num


print('-'*40)
print('MENU PRINCIPAL'.center(40))
print('-'*40)
print('\033[0:32m1 - \033[0:34mVer Pessoas cadastradas\033[m')
print('\033[0:32m2 - \033[0:34mCadastrar novas pessoas\033[m')
print('\033[0:32m3 - \033[0:34mSair do sistema\033[m')
print('-'*40)
print(f'Opção: {valida()}'.center(40))
print('-'*40)


# 115b: Vamos ver como fazer acesso a arquivos usando o Python.

# 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
