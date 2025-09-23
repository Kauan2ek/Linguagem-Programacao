# Crie um programa que leia um número inteiro e verifique se ele é múltiplo de 3 e de 5 ao mesmo tempo.
n = int(input('Número: '))

if n % 3 == 0 and n % 5 == 0:
    print(f'{n} é divisível por 3 e por 5')