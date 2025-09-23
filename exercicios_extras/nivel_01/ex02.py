# Crie um programa que leia a idade de uma pessoa e informe em qual faixa etária ela se encontra:
# - Criança: até 12 anos
# - Adolescente: 13 a 17 anos
# - Adulto: 18 a 59 anos
# - Idoso: 60 anos ou mais
idade = int(input('Idade: '))

if idade < 0:
    print('Idade inválida!')
elif idade < 13:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')
