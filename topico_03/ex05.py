# Faça um programa que leia um número inteiro e mostre 
# na tela se é ou não um número primo.

n = int(input('Número inteiro: ')) # 17

if n <= 1:
    print('Não é um número primo!')
else:
    for i in range(2, n // 2):
        if n % i == 0:
            print(f'{n} não é um número primo!')
            break
    else:
        print(f'{n} é número primo!')