# Faça um programa que faça a entrada de um texto. 
# Se for um e-mail, retorne "E-mail válido", caso contrário,
# retorne "E-mail inválido". Para tanto, verifique se o texto
# possui o símbolo @
email = input('Digite um email: ')

# Solução 1
for caracter in email:
    if '@' == caracter:
        print('E-mail válido')
        break
else:
    print('E-mail inválido')



# Solução 2
if '@' in email:
    print('Email válido!')
else:
    print('Email inválido!')

