# Faça um programa que leia vários números inteiros (parando apenas quando o usuário digitar 0) e mostre no final:
# - a soma de todos os números
# - a quantidade de números digitados
# - a média deles

n = None
qtd = -1 # começa em menos um pra compensar o 0 no final
soma = 0
while n != 0:
    n = int(input(f'{qtd + 1}° Número: '))
    soma += n

    qtd += 1

media = soma / qtd
print(f'''
    Soma: {soma}
    Quantidade: {qtd}
    Média: {media}
''')