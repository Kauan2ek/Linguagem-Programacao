# Faça um programa que mostre a tabuada de um 
# número informado.
n = int(input('Número: '))

i = 1
while i <= 10:
    print(f'{n} x {i} = {n * i}')
    i += 1