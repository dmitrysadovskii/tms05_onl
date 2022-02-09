"""HOMEWORK TASK NUMBER ONE
THIS CODE IS A GAME: BULLS AND COWS
"""


comp = 5456
computer = str(comp)


def cows_and_bulls_game(computer):
    bulls = 0
    cows = 0
    while True:
        try:
            player = str(int(input("Input number: ")))
            if len(player) != 4:
                print("Oops, the length should be 4 numbers")
                continue
            elif player[0] == player[1] or \
                    player[1] == player[2] or player[2] == player[3]:
                print("Oops, there should be no repetitive numbers")
                continue
            else:
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
            break
        except ValueError:
            print("Please enter the integer. Example: 1234")


cows_and_bulls_game(computer)
