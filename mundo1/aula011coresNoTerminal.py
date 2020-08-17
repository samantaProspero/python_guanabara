# Cores no terminal
'''
codigo ansci

códigos para estilo: 
0 none
1 bold
4 undeline
7 inverte colorações entre fonte e fundo

codigos para cor da fonte:
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza

cores de background:
são as mesmas cores das fontes
a numeração vai de 40 a 47

\033[(style); (cor do texto) , (cor do bg)m

\033[0:33:44m

print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7:30:43mOlá, Mundo!\033[m')
print('\033[4:34:43mOlá, Mundo!\033[m')
print('\033[1:30:46mOlá, Mundo!\033[m')
print('\033[1:30:40mOlá, Mundo!\033[m')
'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))
# outra forma:
nome = 'Guanabara'
print('Olá {}{}{}.'.format('\033[36m', nome,'\033[m'))

# terceira maneira:
nome = 'Guanabara'
cores = { 'limpa': '\033[m',
          'branco': '\033[30m',
          'vermelho': '\033[31m',
          'verde': '\033[32m',
          'amarelo': '\033[33m',
          'azul': '\033[34m',
          'magenta': '\033[35m',
          'ciano': '\033[36m',
          'cinza': '\033[37m',
          'pretoebranco': '\033[7:30m'}
print('Olá {}{}{}.'.format(cores['azul'], nome, cores['limpa']))
print('{}branco{}'.format(cores['branco'], cores['limpa']))
print('{}vermelho{}'.format(cores['vermelho'], cores['limpa']))
print('{}verde{}'.format(cores['verde'], cores['limpa']))
print('{}amarelo{}'.format(cores['amarelo'], cores['limpa']))
print('{}azul{}'.format(cores['azul'], cores['limpa']))
print('{}magenta{}'.format(cores['magenta'], cores['limpa']))
print('{}ciano{}'.format(cores['ciano'], cores['limpa']))
print('{}cinza{}'.format(cores['cinza'], cores['limpa']))