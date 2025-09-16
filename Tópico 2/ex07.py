# Faça um programa para jogar Jokenpô (clássico pedra, papel
# e tesoura) com você. Você deverá informar uma das opções,
# o programa deverá então sortear uma das três opções possíveis
# e mostrar quem ganhou na tela.
from random import choice


def jokenpo():
    opcoes = ("pedra", "papel", "tesoura")
    programa = choice(opcoes)

    print(f"programa: {programa}")

    jogador = input('Pedra, papel, tesoura... ').lower()

    if jogador not in opcoes:
        print('Valor inválido!!')
        return False

    if programa == 'pedra':
        if jogador == 'papel':
            print('Você ganhou!')
        elif jogador == 'tesoura':
            print('Você perdeu!')
        else:
            print('Empate!')
    elif programa == 'papel':
        if jogador == 'pedra':
            print('Você perdeu!')
        elif jogador == 'papel':
            print('Empate!')
        else:
            print('Você ganhou!')
    else:
        if jogador == 'pedra':
            print('Você ganhou!')
        elif jogador == 'papel':
            print('Você perdeu!')
        else:
            print('Empate!')


jokenpo()
