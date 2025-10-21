# Uma técnica muito comum para apresentar uma Word Cloud é
# contar a frequência de palavras em um texto para destacar
# a fonte de cada palavra. Para isso, crie um programa que
# leia uma string, por exemplo "Python é incrível e Python
# é simples", e retorne o dicionário: {'Python': 2, 'é': 2,
# 'e': 1, 'incrível': 1, 'simples': 1}.
frase = 'Python é incrível e Python é simples'
frase = frase.split()

dicionario = {}

for palavra in frase:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

# Outra solução:
# for palavra in frase.split():
#     dicionario[palavra] = dicionario.get(palavra, 0) + 1



print