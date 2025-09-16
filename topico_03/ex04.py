# Faça um programa que leia um número inteiro
# N e mostre na tela os N primeiros números da 
# Sequência de Fibonacci.
# Por exemplo, N = 7
# Output: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
# Lê o número inteiro N
n = int(input("Digite um número inteiro: "))

a = 0
b = 1

contador = 1

print(a, end=' ')

while contador < n:
    print('->', b, end=' ')
    a, b = b, a + b
    contador += 1

