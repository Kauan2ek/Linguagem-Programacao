# Faça um programa que peça ao usuário para digitar uma senha. Enquanto a senha for diferente de "1234", continue pedindo. Quando for igual, mostre "Acesso permitido".

while True:
    senha = input('Senha: ')
    if senha == '1234':
        print('Acesso permitido.')
        break
    print('Senha incorreta!')
