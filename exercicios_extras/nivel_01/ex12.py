# Faça um programa que leia 5 números inteiros e mostre qual foi o maior e qual foi o menor.
numeros = [0, 0, 0, 0, 0]
n = int(input(f'Digite o 1° número: '))
numeros[0] = n

maior = n
menor = n

for i in range(1, 5):
    n = int(input(f'Digite o {i + 1}° número: '))

    if (n > maior):
        maior = n
    elif(n < menor):
        menor = n

    numeros[i] = n

print(f'''
    {numeros}
    Maior: {maior}
    Menor: {menor}
''')