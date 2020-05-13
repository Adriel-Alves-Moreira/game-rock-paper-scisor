from time import sleep
from random import randint
pc = randint(1, 3)
print('-=--' *20)
print('Vamos jogar "Pedra, Papel, Tesoura"')
print('-=--' *20)
player = int(input(" [1] Pedra\n [2] Papel\n [3] Tesoura\n "))
if pc == 1:
    if pc == player:
        print('EMPATE!')
    elif player == 3:
        print('BOT WINS!')
    elif player == 2:
        print('PLAYER WINS!')
elif pc == 2:
    if pc == player:
        print('EMPATE!')
    elif player == 1:
        print('BOT WINS!')
    elif player == 3:
        print('PLAYER WINS!')
elif pc == 3:
    if pc == player:
        print('EMPATE!')
    elif player == 1:
        print('PLAYER WINS!')
    elif player == 2:
        print('BOT WINS!')
elif player != 1 or 2 or 3:
    print('Nao existe esssa opçao')
