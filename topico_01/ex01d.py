# Faça um programa que leia o preço de um produto e mostre o valor com 5% de desconto.
preco = float(input("Digite o preço do produto: R$"))

valor_final = preco * 0.95

print(f"O valor do produto é de R${valor_final:.2f}")