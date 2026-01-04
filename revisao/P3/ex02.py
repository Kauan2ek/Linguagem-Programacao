# Crie um programa que:
# 1. Tenha uma função cadastrar_produto(nome, preço)
# 2. Salve os produtos em um arquivo produtos.json
# 3. Tenha uma função para mostrar todos os produtos
# 4. Tenha outra para buscar produtos acima de determinado valor
import json
caminho = 'revisao/P3/produtos.json'

# 1 e 2. Tenha uma função cadastrar_produto(nome, preço)
def cadastrar_produto(nome='TV', preco=1200.99):
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
        if (len(linhas) < 2):
            conteudo = '{' + f'\n\t"{nome}": ' + f'{preco}\n' + '}'
        else:
            linhas = ''.join(linhas)
            conteudo = linhas[:-2] + linhas[-1][:-2] + \
                f',\n\t"{nome}": {preco}\n' + '}'

    with open(caminho, 'w') as arquivo:
        arquivo.write(conteudo)

    return conteudo

# 3. Tenha uma função para mostrar todos os produtos
def mostrar_produtos():
    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()

        return json.loads(conteudo)

# 4. Tenha outra [função] para buscar produtos acima de determinado valor
def filtrar_produtos(valor):
    with open(caminho, 'r') as arquivo:
        arq = arquivo.read()
        produtos = json.loads(arq)

    produtos_filtrados = {}
    for (key, value) in produtos.items():
        if value > valor:
            produtos_filtrados[key] = value

    return produtos_filtrados


# print(cadastrar_produto('Mouse', 90.90))
print(filtrar_produtos(500))
