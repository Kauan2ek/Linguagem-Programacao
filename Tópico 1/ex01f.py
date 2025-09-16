# Crie um programa que leia dois números e uma operação (soma, subtração, multiplicação ou divisão)
# do usuário. Realize a operação correspondente e mostre o resultado.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = int(input('''
    Qual operação você deseja fazer?
    (1) Soma
    (2) Subtração
    (3) Multiplicação
    (4) Divisão
'''))

match operacao:
    case 1:
        resultado = n1 + n2
    case 2:
        resultado = n1 - n2
    case 3:
        resultado = n1 * n2
    case 4:
        resultado = n1 / n2
    case _:
        print("Operação inválida! Tente novamente...")
        quit()

print(f"Resultado: {resultado}")