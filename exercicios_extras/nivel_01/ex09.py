# Escreva um programa que leia uma frase e conte quantas palavras existem nela.
frase = input('Frase: ')
palavras = frase.split()

print(f'Essa frase possui {len(palavras)}')
