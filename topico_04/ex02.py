# Faça um programa que gere 10 números inteiros.
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.
import random
lista = random.choices(range(0, 5), k=10)
lista_corrigida = []
print(sorted(lista))

for n in lista:
    if n not in lista_corrigida:
        lista_corrigida.append(n)
print(sorted(lista_corrigida))