# Escreva um programa que receba a nota de duas provas de um aluno. Se a média for maior ou igual a 7, mostre “Aprovado”, senão mostre “Reprovado”.
p1 = float(input('Prova 1: '))
p2 = float(input('Prova 2: '))

media = (p1 + p2) / 2

if media >= 7.0:
    print('Aprovado')
else:
    print('Reprovado')