# Leia 10 números e coloque-os em uma lista.
# Depois, mostre:
# Somente os números únicos (sem repetição)
# Quantidade de números repetidos
# Quais números estão repetidos
numeros = [2, 4 ,4 ,4 ,6 ,4 ,56 ,3 , 3, 10, 3, 3, 56]
sem_repeticao = list(set(numeros))

numeros_repetidos = {}
for n in sem_repeticao:
    if numeros.count(n) > 1:
        numeros_repetidos[f"{n}"] = f'{numeros.count(n)} vezes'

print(numeros_repetidos)
