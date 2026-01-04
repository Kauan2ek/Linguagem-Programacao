# Peça ao usuário uma frase e crie um dicionário onde:
# - chave = palavra
# - valor = quantidade de vezes que aparece
# Depois, mostre:
# - O dicionário completo
# - A palavra mais frequente
frase = 'Uma frase qualquer com qualquer uma palavra de uma frase frase só vez'

palavras_unicas = set(frase.lower().split())
print(palavras_unicas)

dicionario = {}
maior_frequencia = 0
mais_frequente = ''
for palavra in palavras_unicas:
    dicionario[palavra] = frase.count(palavra)
    if frase.count(palavra) > maior_frequencia:
        maior_frequencia = frase.count(palavra)
        mais_frequente = palavra


print(dicionario)
print(mais_frequente, maior_frequencia)