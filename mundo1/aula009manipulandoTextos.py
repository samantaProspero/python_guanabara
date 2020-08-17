# strings:
frase = 'Curso em Vídeo Python'
print(frase)

# regras de fatiamento:
print(frase[9])  #retorna V, a decima letra
print(frase[9:13])  # retorna do 9 ao 12
print(frase[9:21:2])  # vai do 9 ao 12, pulando de 2 em 2 retorna VdoPto
print(frase[:5])  # retorna do 0 ao 4
print(frase[15:])  # retorna do 15 ao final
print(frase[9::3])  # retorna do 9 ao final, pulando de 3 em 3

# Análise
print(len(frase)) #length
print(frase.count('o')) # conta as letras o
print(frase.count('o', 0, 13)) # contagem com fatiamento, conta as letras 'o' nas casas 0 a 12
print(frase.find('deo')) # encontra deo e fala onde começa o primeiro match
print(frase.find('android')) # retorna -1, não foi encontrado
print('Curso' in frase) # retorna booleano

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #torna a primeira letra da string maiúscula e deixa as outras minúsculas
print(frase.title()) #torna a primeira letra de cada palavra da string maiúscula

novafrase = '   Aprenda Python   '
print(novafrase)

print(novafrase.strip()) # remove os espaços em branco do inicio e do fim da string
print(novafrase.rstrip()) # remove os espaços em branco do fim da string
print(novafrase.lstrip()) # remove os espaços em branco do inicio da string

# Divisão
print(frase.split()) # separa em várias string, corta no espaço e retorna ['Curso', 'em', 'Vídeo', 'Python']
separado = frase.split()
print('-'.join(separado)) # junta novamente ligando por '-', retorna: Curso-em-Vídeo-Python

# imrime respeitando as quebras de linha
print("""" Mussum Ipsum, cacilds vidis litro abertis. 
Nec orci ornare consequat. Praesent lacinia ultrices consectetur. 
Sed non ipsum felis. Aenean aliquam molestie leo, vitae iaculis nisl. 
Detraxit consequat et quo num tendi nada. Não sou faixa preta cumpadi, sou preto inteiris, inteiris.""")

