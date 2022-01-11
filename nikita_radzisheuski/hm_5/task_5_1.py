"""HOMEWORK TASK NUMBER ONE
THIS CODE IS A GAME: BULLS AND COWS
"""

import random

comp = random.randrange(1000, 9999)
computer = str(comp)


def cows_and_bulls_game(computer):
    player = input("Input the number: ")
    bulls = 0
    cows = 0
    for x, y in enumerate(zip(player, computer)):
        if y[0] in computer and not y[0] == y[1]:
            cows += 1
        elif y[0] == y[1]:
            bulls += 1
    if bulls == 4:
        print(f"You win!,the number is {computer}")
    else:
        print(f'Cows: {cows}, Bulls: {bulls}')
        cows_and_bulls_game(computer)


cows_and_bulls_game(computer)
