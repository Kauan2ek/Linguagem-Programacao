# Escreva um programa que leia o salário de um
# funcionário e calcule o seu aumento. Caso o 
# salário atual seja superior a R$ 1.000,00 
# calcule um aumento de 10%, caso contrário, 
# calcule um aumento de 15%.

salario = float(input('Salário: '))

if salario > 1000:
    salario_ajustado = salario * 1.10
else:
    salario_ajustado = salario * 1.15

print(f'O novo salário é de R${salario_ajustado}.')