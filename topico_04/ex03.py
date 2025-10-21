# Faça um programa que crie uma lista vazia. Em seguida,
# o usuário deverá informar as notas de trabalhos obtidas
# (pode variar de 0 até quantos trabalhos forem informados).
# Por fim, mostre a média aritmética das notas obtidas.
lista = []

qtd_notas = int(input('Quantidade de notas: '))
for i in range(qtd_notas):
    lista.append(float(input('Nota: ')))

soma = 0
for n in lista:
    soma += n
media = soma / qtd_notas

print(round(media, 2))