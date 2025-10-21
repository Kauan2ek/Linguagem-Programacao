# Implemente o jogo da forca. Um usuário deverá entrar
# com uma palavra. Em seguida, outro usuário deverá
# indicar as letras dessa palavra. Caso exista, deverá
# ser mostrada as letras e as suas posições na palavra.
# Caso não exista, o usuário perderá uma chance. No total,
# o usuário terá 6 chances para acertar.
import os
palavra = input('Palavra: ')
os.system('cls')

tries = 0
saida = '_' * len(palavra)
while tries < 6:
    tentativa = input('Letra: ')

    for index, letra in enumerate(palavra.lower()):
        saida = list(saida)
        if letra == tentativa.lower() and saida:
            saida[index] = letra


    if ''.join(saida).lower() == palavra.lower() or tentativa.lower() == palavra.lower():
        print('Você venceu!')
        break
    print(' '.join(saida))
    
    tries += 1
else:
    print(f'Você perdeu... \nA palavra era: {palavra}.')