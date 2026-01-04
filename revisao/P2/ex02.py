# Peça ao usuário 8 números e guarde em uma lista.
# Depois, crie uma nova lista contendo somente os números pares digitados.
# Mostre a lista original e a lista de pares.
numeros = list()
# for i in range(8):
#     numeros.append(int(input('Numero: ')))
numeros = [12, 3, 4, 6, 1, 6, 8, 9]

numeros_pares = []
for n in numeros:
    if n % 2 == 0:
        numeros_pares += 1