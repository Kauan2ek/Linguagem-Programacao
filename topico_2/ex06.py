# Faça um program que leia o ano de nascimento de uma
# pessoa e informe se ele ainda vai se alistar ao serviço
# militar ou se ele está no período de se alistar ou se
# ele perdeu o prazo para se alistar. Além disso, mostre
# também a quantidade de anos que falta para se alistar
# ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
print(ano_atual)
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc

if idade < 18:
    print(f'Você precisa se alistar ao serviço militar daqui a {18 - idade} anos.')
elif idade == 18:
    print('Você está em período de alistamento!')
else:
    print(f'Você deveria ter se alistado há {idade - 18} anos.')