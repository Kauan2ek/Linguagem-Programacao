# Faça um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O usuário deverá informar o valor
# da casa, a quantidade de parcelas que deseja pagar e seu
# salário. O empréstimo deverá ser negado caso o valor da
# parcela exceda 30% do salário.
valor_casa = float(input('Valor da casa: R$'))
qtd_parcelas = int(input('Quantidade de parcelas: '))
salario = float(input('Salário: R$'))

valor_parcela = valor_casa / qtd_parcelas

if valor_parcela < salario * 0.30:
    print('Empréstimo aprovado!')
else:
    print('Emprestimo recusado!')
