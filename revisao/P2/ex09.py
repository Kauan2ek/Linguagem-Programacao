# Peça ao usuário uma frase.
# Transforme em conjunto para obter apenas as palavras únicas.
# Depois:
# - Mostre o conjunto
# - Mostre quantas palavras únicas existem
# - Mostre as palavras em ordem alfabética
# Exemplo:
# Entrada:
# "eu gosto de aprender python e eu gosto de programar"
# Saída:
# {'eu', 'gosto', 'de', 'aprender', 'python', 'e', 'programar'}
# 7 palavras únicas
frase = 'eu gosto de aprender python e eu gosto de programas'

frase_s_repeticao = set(frase.split())
palavras_unicas = len(frase_s_repeticao)
print(sorted(list(frase_s_repeticao)))
print(f'{palavras_unicas} palavras únicas')