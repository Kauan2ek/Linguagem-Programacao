# Peça ao usuário para digitar 10 nomes.
# Se houver nomes repetidos, numere-os automaticamente.
nomes = ['Pedro', 'João', 'Pedro', 'João', 'Pedro', 'Maria', 'Maria', 'Carlos']

for nome in nomes:
    if nomes.count(nome) > 1:
        qtd = 1
        while nome in nomes:
            nomes[nomes.index(nome)] = f'{nome} {qtd}'
            qtd += 1

print(nomes)
