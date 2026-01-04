# Leia duas listas com nomes de alunos:
# - Lista A: alunos presentes na segunda-feira
# - Lista B: alunos presentes na terça-feira
# Transforme em conjuntos e mostre:
# - Alunos que vieram nos dois dias
# - Alunos que vieram apenas segunda
# - Alunos que vieram apenas terça
# - Todos que vieram pelo menos um dia
alunos_seg = set(['João', 'Carlos', 'Pedro', 'Lucas'])
alunos_ter = set(['Kauan', 'Pedro', 'João', 'Maria'])

print(alunos_seg.intersection(alunos_ter))
print(alunos_seg - alunos_ter)
print(alunos_ter - alunos_seg)
print(alunos_seg.union(alunos_ter))