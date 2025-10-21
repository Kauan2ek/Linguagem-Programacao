# Uma tarefa comum em NLP (Natural Process Language)
# é substituir palavras por sinônimos para
# simplificação de texto, padronização ou expansão
# semântica. Isso é útil em aplicações
# como geração de textos ou normalização de linguagem.
# Com base neste contexto, crie um programa em Python
# que receba como entrada uma frase e, com base no
# dicionário de sinônimos, onde a chave é uma palavra
# original e o valor é sua substituição, retorne a frase
# modificada com as substituições aplicadas.

sinonimos = {'estudante': 'aluno', 'feliz': 'contente', 'prova': 'exame'}

# Exemplo:
# Input: O estudante está feliz porque passou na prova
# Output: O aluno está contente porque passou na exame

frase = 'O estudante está feliz porque passou na prova'
frase_corrigida = frase.split()

# print(frase)

for index, palavra in enumerate(frase_corrigida):
    if palavra in sinonimos:
        frase_corrigida[index] = sinonimos.get(palavra)
    # print(index, palavra)

frase_corrigida = ' '.join(frase_corrigida)
print(frase_corrigida)
