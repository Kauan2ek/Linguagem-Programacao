# Escreva um programa que receba três valores numéricos representando
# os lados de um triângulo e determine se os valores podem formar um
# triângulo válido (a soma de dois lados deve ser sempre maior que o
# terceiro). Se for válido, classifique-o como: Equilátero: todos os
# lados iguais; Isósceles: dois lados iguais; ou Escaleno: todos os
# lados diferentes.
lados = []

for i in range(0, 3):
    lados.append(float(input(f'{i + 1}° lado: ')))

a, b, c = lados

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Triângulo equilátero')
    elif a != b and b != c and a != c:
        print('Triângulo escaleno!')
    else:
        print('Triângulo isósceles!')
else:
    print('Triângulo inválido!')
    