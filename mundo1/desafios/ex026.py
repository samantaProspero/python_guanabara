# Crie um programa que leia uma frase e mostre:
# Quantas letras 'a' tem;
# Em que posição aparece o primeiro 'a' ;
# Em que posição aparece o último 'a' ;

frase= str(input('Digite uma frase: ')).lower()
letraA = frase.count('a')
print('São {} letras "a"'.format(letraA))
print('O primeiro "a" está na posição: {}'.format(frase.find('a') + 1))
print('O último "a" está na posição: {}'.format(frase.rfind('a') + 1))
