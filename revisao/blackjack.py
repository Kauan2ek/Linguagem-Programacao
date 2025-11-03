# Implemente em Python um jogo de cartas 21 (Blackjack simplificado),
# utilizando as estruturas de dados dict e list. O jogo
# deve permitir que o jogador dispute contra o computador, somando valores
# de cartas até chegar o mais próximo possível de 21 pontos, sem ultrapassar
# esse valor. Cada carta deve ser representada como um dicionário contendo
# o número e o naipe, e o baralho deve ser uma lista embaralhada de cartas.
# O jogador e o computador devem receber duas cartas iniciais, e novas cartas
# podem ser retiradas do sempre do final do baralho. O programa deve
# exibir as cartas e pontuações finais, indicando o vencedor. Utilize o
# código abaixo como base para a definição dos naipes:

# Set up the constants:
import random, os
HEARTS = chr(9829)    # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)    # Character 9824 is '♠'
CLUBS = chr(9827)     # Character 9827 is '♣'


baralho = []
for i in range(1, 11):
    baralho.append({'numero': i, 'naipe': HEARTS})
    baralho.append({'numero': i, 'naipe': DIAMONDS})
    baralho.append({'numero': i, 'naipe': SPADES})
    baralho.append({'numero': i, 'naipe': CLUBS})


random.shuffle(baralho)

computer = [baralho.pop(), baralho.pop()]
points_computer = computer[0]["numero"] + computer[1]['numero']

while points_computer < 17:
    computer.append(baralho.pop())
    points_computer += computer[-1]["numero"]

user = [baralho.pop(), baralho.pop()]
points_user = user[0]["numero"] + user[1]['numero']
print(user, points_user, end='\n\n\n---------')

while True:
    os.system('cls')
    print(f"Suas cartas são: {user[0]['numero']} {user[1]['naipe']}", end='')
    for carta in user[1:]:
        print(f" | {carta['numero']} {carta['naipe']}", end='')

    print("\nPontos: ", points_user)
    
    if points_user > 21:
        break

    if input('\n\nQuer tirar mais uma? [S/N] ').lower() == 's':
        user.append(baralho.pop())
        points_user += user[-1]['numero']
    else:
        break

if points_user == points_computer:
    print("Empate!!!")
elif points_user > 21:
    if points_computer > 21:
        print("Empate!!!")
    else:
        print("Você perdeu!!!")
else:
    if points_user < points_computer:
        print("Você perdeu!!!")
    else:
        print("Você ganhou!!!")      


print('\n***Computador***')
print(f"Cartas do computador: {computer[0]['numero']} {computer[1]['naipe']}", end='')
for carta in computer[1:]:
    print(f" | {carta['numero']} {carta['naipe']}", end='')
print(f'\nPontuação do computador: {points_computer}')