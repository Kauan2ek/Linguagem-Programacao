# Escreva um programa que leia um número inteiro e mostre a tabuada dele de 1 até 20 (não só até 10).
n = int(input('Número: '))

for i in range(1, 21):
    print(f'{n} x {i} = {n * i}')