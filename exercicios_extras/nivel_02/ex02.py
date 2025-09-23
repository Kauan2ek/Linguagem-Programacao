# Faça um programa que leia um número inteiro positivo N e mostre a soma de todos os números ímpares de 1 até N.
n = int(input('Digite um número: '))

somatorio = 0
for i in range(1, n, 2):
    somatorio += i

print('Somatório: ', somatorio)