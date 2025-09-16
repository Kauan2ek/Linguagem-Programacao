# Implemente um programa que leia 4 notas de um aluno e mostre a média aritmética.
notas = []
media = 0
for i in range(0, 4):
    notas.append(float(input(f"Digite a {i + 1}° nota: ")))
    media += notas[i]
media = media / (i + 1)
print(f"A média é: {media:.2f}.")
print(f"A média é: {round(media, 2)}.")