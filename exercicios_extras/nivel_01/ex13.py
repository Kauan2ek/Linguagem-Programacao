# Escreva um programa que calcule o fatorial de um número usando laço for.
n = int(input('Número: '))

fatorial = 0
for i in range(n, 0, -1):
    fatorial += i
    print(f'i: {i}  /// n: {n}')

print(f'{n}! = {fatorial}')