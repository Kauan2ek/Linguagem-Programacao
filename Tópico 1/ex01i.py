# Peça ao usuário para informar o raio de um círculo e calcule a sua área. A fórmula da área do círculo é:
# 𝐴 = 𝜋 × 𝑟2
# Onde 𝑟 é o raio e 𝜋 é aproximadamente 3.14159.
PI = 3.14159

raio = float(input("Digite "))
area = PI * pow(raio, 2) 

print(f"Área: {round(area, 2)}")