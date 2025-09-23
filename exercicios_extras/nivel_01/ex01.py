# Escreva um programa que receba dois números e mostre qual deles é o maior, ou se são iguais.
n1 = int(input('Digite um primeiro n°: '))
n2 = int(input('Digite o segundo n°: '))

if n1 > n2:
    print(f'{n1} > {n2}')
elif n1 < n2:
    print(f'{n2} > {n1}')
else:
    print(f'{n1} = {n2}')
