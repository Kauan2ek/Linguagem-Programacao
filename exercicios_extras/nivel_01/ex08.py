# Faça um programa que receba uma temperatura em graus Celsius e converta para Fahrenheit.
# °F = (°C × 1,8) + 32
graus = float(input('°C: '))
fahrenheit = (graus * 1.8) + 32

print(f'{graus}°C = {round(fahrenheit, 2)}°F')