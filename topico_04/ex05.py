# Faça um programa em que o usuário deverá digitar
# os nomes de dez alunos da sala de aula. Em seguida,
# caso o programa encontre nomes repetidos, ele deverá
# alterar o nome adicionando o número sequencial. Por
# exemplo, se na lista tivermos dois "José", após o
# processamento a lista deverá conter "José 1" e "José 2".
N = 4  # 10
nomes = []

for i in range(N):
    nomes.append(input(f'Nome {i + 1}: '))

# nomes = ['Pedro', 'Maria', 'Carlos', 'Pedro', 'Maria', 'Joao', 'Pedro', 'Pedro', 'Maria', 'Pedro']

for index, pessoa in enumerate(nomes):

    quantidade = 1
    if nomes.count(pessoa) > 1:
        for i, nome in enumerate(nomes):
            if pessoa == nome:
                nomes[i] = f'{pessoa} {quantidade}'
                quantidade += 1

print(nomes)
