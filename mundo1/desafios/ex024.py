# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"
cidade = (input("Digite o nome de uma cidade: ")).strip()
print(cidade.lower()[:5] == "santo")

