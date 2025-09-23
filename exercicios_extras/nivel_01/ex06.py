# Escreva um programa que calcule a soma de todos os números de 1 até N, onde N deve ser informado pelo usuário.
n = int(input('Digite um número: '))

somatorio = 0
for i in range(1, n + 1):
    somatorio += i

print(f'Somatório: {somatorio}')