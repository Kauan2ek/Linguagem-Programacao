# Faça um programa que carregue uma lista com dez
# números inteiros, informados pelo usuário. Em seguida,
# crie e mostre uma lista resultante ordenada de maneira
# crescente e crie e mostre uma lista resultante ordenada
# de maneira decrescente.
numeros = []
for i in range(10):
  numeros.append(int(input('Digite um número: ')))
print(numeros)
crescente = sorted(numeros)
decrescente = sorted(numeros, reverse=True)

print('Crescente: ', crescente)
print('Descrescente: ', decrescente)