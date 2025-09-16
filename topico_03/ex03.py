# Escreva um programa que leia um número inteiro
# qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número inteiro: '))

fatorial = n

while n > 1:
    n -= 1
    fatorial *= n

print(f'{n}! = {fatorial}')