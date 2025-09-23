# Escreva um programa que leia a temperatura em Celsius e converta para Fahrenheit. A fórmula de conversão é:
# 𝐹  = 𝐶 × 9/5  + 32
celsius = float(input("Temperatura em °C: "))
fahrenheit = celsius * 9/5 + 32

print(f"Temperatura em °F: {round(fahrenheit, 1)}")