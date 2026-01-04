# Peça ao usuário uma lista com 6 nomes.
# Depois, peça um nome para busca.
# Mostre se o nome está na lista.
# Se estiver, diga em qual posição ele aparece.
nomes = ['Kauan', 'Júlio', 'Carlos', 'Pedro', 'Tiago', 'João']

busca = input('Busca: ')
if busca in nomes:
    print(f"O nome está na lista! Na {nomes.index(busca) + 1}° posição")
else:
    print(f"{busca} não está na lista :(")