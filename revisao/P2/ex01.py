# Faça um programa que leia o nome completo de uma pessoa e mostre:
# Quantas letras tem o nome (sem contar espaços)
# Quantas palavras ele possui
# O nome invertido
nome = 'Kauan Talles Silva Dias'

qtd_letras = len(list(nome.replace(' ', '')))
print("Qtd Letras: ", qtd_letras)

qtd_palavras = len(nome.split())
print("Qtd palavras: ",qtd_palavras)

nome_invertido = nome[::-1]
print("Invertido: ", nome_invertido)
