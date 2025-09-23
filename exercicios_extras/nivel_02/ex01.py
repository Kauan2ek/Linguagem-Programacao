# Crie um programa que leia dois números inteiros e mostre todos os números no intervalo entre eles.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo  número: '))

for i in range (n1 + 1, n2):
    print(i)