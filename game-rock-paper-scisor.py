from time import sleep
from random import randint
while True:
    pc = randint(1, 3)
    print('-=--' *20)
    print('Vamos jogar "Pedra, Papel, Tesoura"')
    print('-=--' *20)
    player = int(input(" [1] Pedra\n [2] Papel\n [3] Tesoura\n "))
    if pc == 1:
        if pc == player:
            print('EMPATE! Voces dois escolheram Pedra')
        elif player == 3:
            print('BOT WINS! Porque voce escolheu Tesoura e ele Pedra')
        elif player == 2:
            print('PLAYER WINS! Porque voce escolheu Papel e ele Pedra')
    elif pc == 2:
        if pc == player:
            print('EMPATE! Voces dois escolheram Papel')
        elif player == 1:
            print('BOT WINS! Porque voce escolheu Pedra e ele Papel')
        elif player == 3:
            print('PLAYER WINS! Porque voce escolheu Tesoura e ele Papel')
    elif pc == 3:
        if pc == player:
            print('EMPATE! Voces dois escolheram Tesoura')
        elif player == 1:
            print('PLAYER WINS! Porque voce escolheu Pedra e ele Tesoura')
        elif player == 2:
            print('BOT WINS! Porque voce escolheu Papel e ele Tesoura')
    sleep(5)
    print('\nVoce quer jogar de novo?')
    play = int(input(' [1] Sim\n [2] Nao\n'))
    if play == 1:
        print('\nVamos la!!')
    else:
        break
