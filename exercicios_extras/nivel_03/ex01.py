# Faça um programa que leia um número inteiro N e verifique se ele é perfeito.
# 👉 (Um número é perfeito quando a soma dos seus divisores próprios é igual a ele. Exemplo: 6 → 1+2+3=6).
n = int(input('Número: '))

divisores = 0
metade = int(round((n / 2), 0))
for i in range(1, metade + 1):
    if n % i == 0:
        divisores += i
        print(i, end='')
        if i != n / 2 and n % i == 0:
            print(' + ', end='')

if divisores == n:
    print(f' = {n} é um número perfeito!')
else:
    print(f' ≠ {n} não é um número perfeito!')