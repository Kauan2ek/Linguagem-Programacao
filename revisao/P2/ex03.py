# Peça ao usuário 7 números e armazene-os em uma lista.
# Mostre:
# - A lista original
# - A lista ordenada
# - Quantos números são pares
# - Quantos números são positivos
numeros = [2, -3, -1, 5, 6, -3, 8]

# for i in range(7):
#     numeros.append(int(input('Número: ')))
lista_ordenada = sorted(numeros)

qtd_pares = 0
qtd_positivos = 0
for n in numeros:
    print('\n', n)
    if n % 2 == 0:
        qtd_pares += 1
        print('par', end='\t')
    if n > 0:
        qtd_positivos += 1
        print('positivo')

print(numeros)
print(lista_ordenada)
print('Qtd pares: ', qtd_pares)
print('Qtd positivos: ', qtd_positivos)