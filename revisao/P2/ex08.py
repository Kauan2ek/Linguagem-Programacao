# Peça ao usuário 5 nomes e 5 idades (na mesma ordem).
# Guarde em um dicionário assim:
# {"Ana": 17, "Pedro": 16, "Lucas": 18, ...}
# Depois, mostre:
# - Quem é o mais velho
# - Quem é o mais novo

dicionario = {}
for i in range(2):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    dicionario[nome] = idade

print(dicionario)

