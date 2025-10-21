# Faça um programa que contenha duas listas com 5 posições.
# Na primeira lista, deverá ser inserido o nome dos alunos.
# Na segunda lista, na mesma posição, a nota do aluno. Em
# seguida, mostre o nome dos alunos com a maior e a menor nota.
N = 3
nomes = []
notas = []

for i in range(N):
    nomes.append(input('Nome: '))
    notas.append(float(input('Nota: ')))
    print('----------------------------')

maior_nota = [notas[0], nomes[0]]
menor_nota = [notas[0], nomes[0]]
for i in range(N):
    if notas[i] > maior_nota[0]:
        maior_nota[1] = nomes[i]
        maior_nota[0] = notas[i]

    if notas[i] < menor_nota[0]:
        menor_nota[1] = nomes[i]
        menor_nota[0] = notas[i]

print(f'Maior: {maior_nota[0]} // Aluno: {maior_nota[1]}')
print(f'Menor: {menor_nota[0]} // Aluno: {menor_nota[1]}')