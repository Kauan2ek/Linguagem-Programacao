# Faça um programa que leia o nome de uma pessoa e mostre quantas vogais esse nome possui.
vogais = ('a', 'e', 'i', 'o', 'u')
nome = input('Nome: ')

nVogais = 0
for letra in nome:
    if letra in vogais:
        nVogais += 1

print(f'Quantidade de vogais: {nVogais}')