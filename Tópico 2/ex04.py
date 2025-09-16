# Faça um programa em que ele sorteie um número entre 0 e 5. 
# O usuário deverá então adivinhar este número e o programa
# deverá escrever na tela se ele acertou ou não.
from random import randint

numero_aleatorio = randint(0, 5)

n = int(input('Digite um número entre 1 e 5: '))

print(f'aleatório: {numero_aleatorio} // n: {n}')
if n == numero_aleatorio:
    print('Você acertou!!')
else:
    print('Você errou!!')