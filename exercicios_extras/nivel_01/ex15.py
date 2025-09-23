# Escreva um programa que leia o nome de várias pessoas (até o usuário digitar "fim") e, ao final, mostre quantos nomes foram digitados e qual foi o maior nome em quantidade de letras.
nomes = []
maiorNome = ''

i = 0
while True:
    nomes.append(input(f'Digite o {i + 1}° nome: '))
    
    if nomes[i].lower() == 'fim':
        nomes.pop()
        break
    
    if nomes[i] == '':
        nomes.pop()

    if len(nomes[i]) > len(maiorNome):
        maiorNome = nomes[i]

    i += 1


print(f'Nomes: {nomes[0]}, ', end='')
for nome in nomes[1:]: # para começar apartir do índice 1 e não repetir o primeiro nome
    print(',', nome, end='')
print(f'\nMaior nome: {maiorNome}')