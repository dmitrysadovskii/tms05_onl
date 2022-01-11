from random import choice
a = '1234567890'
hidden_number = choice(a)
for i in range(3):
    hidden_number += choice(a)

while True:
    y = input('enter 4-digit number:')
    if y == ' ':
        print('Do not enter empy string, try again!')
        break
    elif len(y) != 4:
        print('Only 4 numbs allowed, try again!')
        break

    bulls = 0
    cows = 0
    for i in range(4):
        if hidden_number[i] == y[i]:
            bulls += 1
        elif y[i] in hidden_number:
            cows += 1
    print(y + ' is ' + str(bulls) + ' bulls and ' + str(cows) + ' cows')
    if bulls == 4:
        print('You win!!!!!')
        break
