# Crie uma função que receba o nome de um arquivo .txt, leia o conteúdo e retorne:
# - quantidade de linhas
# - quantidade de palavras
# - palavra mais frequente
# - um dicionário com a frequência de cada palavra
# Depois, mostre tudo na tela.

def frequencia_palavras(nome_arquivo):
    with open(f'revisao/P3/{nome_arquivo}', 'r') as arquivo:
        linhas = arquivo.readlines()

    qtdLinhas = len(linhas)
    texto = ' '.join(linhas)

    # Remover pontuações simples
    for p in ",.!?:;\n":
        texto = texto.replace(p, ' ')

    palavras = texto.split()
    qtdPalavras = len(palavras)

    dicionario = {}
    for palavra in palavras:
        palavra = palavra.lower()
        dicionario[palavra] = dicionario.get(palavra, 0) + 1
    mais_frequente = max(dicionario, key=dicionario.get)

    return (qtdLinhas, qtdPalavras, mais_frequente, dicionario)


linhas, palavras, mais_frequente, dicionario = frequencia_palavras("texto.txt")
print(f'''
Quantidade de linhas: {linhas}
Quantidade de palavras: {palavras}
Palavra mais frequente: {mais_frequente}
Dicionário: {dicionario}

''')
