# arquivo = open('Arquivos/mensagem.txt', 'r')
# print(arquivo.read())
# arquivo.close()

# caminho = r'C:\my\Fatec\2°Semestre\Linguagem-Programacao\Arquivos\mensagem.txt'
# with open(caminho, 'r') as arq:
#     msg = arq.read()

# print('--------------')
# print(msg)


msg = '''A nota de Matemática foi de 9.0'''
caminho = r'C:\my\Fatec\2°Semestre\Linguagem-Programacao\Arquivos\mensagem.txt'
with open('Arquivos/mensagem.txt', 'w') as arquivo:
    arquivo.write(msg)

# adicionando (recriando o arquivo)
with open(caminho) as arquivo:
    conteudo = arquivo.read()

conteudo += '\nA nota de História foi 9.7'

with open(caminho, 'w') as arq:
    arq.write(conteudo)


# Exemplo na prática
disciplinas = ('matematica', 'portugues', 'filosofia', 'historia', 'fisica', 'geografia', 'quimica', 'biologia')
notas = [7.8, 8.2, 9.8, 7.2, 8.5, 7.6, 9.5, 10]

conteudo = []
for i in range(len(notas)):
    conteudo.append(f'A nota de {disciplinas[i]} foi {notas[i]}\n')

with open('Arquivos/boletim.txt', 'w') as arquivo:
    arquivo.writelines(conteudo)