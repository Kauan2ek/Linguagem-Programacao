# Supondo que queremos pintar o muro da instituição, faça um programa que leia a altura e a largura do muro e mostre a quantidade de tinta necessária (1 litro de tinta pode pintar uma área de 2 metros quadrados).
altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))

tinta = altura * largura / 2

print(f"Você precisará de {tinta} litros de tinta")