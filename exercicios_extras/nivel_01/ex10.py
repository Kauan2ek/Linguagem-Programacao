# Faça um programa que leia o valor de uma compra e calcule o valor a ser pago considerando:
# À vista: 10% de desconto
# Parcelado em até 3 vezes: sem desconto
# Parcelado em mais de 3 vezes: juros de 20%
valor_compra = float(input('Valor da compra: '))
a_vista = valor_compra * 0.9
parcelado_ate_3x = valor_compra
parcelado_mais_3x = valor_compra * 1.20

print(f'''
      Valor:      R${valor_compra:.2f}
      À vista:    R${a_vista:.2f}
      Em até 3x:  R${parcelado_ate_3x:.2f}
      Mais de 3x: R${parcelado_mais_3x:.2f}
      ''')
