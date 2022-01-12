hidden_numb = 9652
enter_numb = input('Enter four-digit numbers: ')
enter_numb_list = list(enter_numb)
hidden_numb_list = list(str(hidden_numb))


bulls = 0
cows = 0
unique = set(enter_numb_list)


if len(enter_numb_list) == 0:
    print('Enter numbers')
else:
    if len(enter_numb_list) != 4:
        print('Enter only four-digit number')
    elif len(set(hidden_numb_list)) != len(unique):
        print('numbers should not be repeated ')
    elif enter_numb.islower():
        print('Enter only numbers')
    else:
        for i in hidden_numb_list:
            if i in enter_numb_list:
                if hidden_numb_list.index(i) == enter_numb_list.index(i):
                    bulls += 1
                else:
                    cows += 1

        answer = ''
        if bulls > 0 or cows > 0:
            if cows == 1:
                answer += 'One cow'
            elif cows == 2:
                answer += 'Two cows'
            elif cows == 3:
                answer += 'Three cows'
            elif cows == 4:
                answer += 'Four cows'

            if len(answer) > 0 and 0 < bulls < 4:
                answer += ', '

            if bulls == 1:
                answer += 'One bull'
            elif bulls == 2:
                answer += 'Two bulls'
            elif bulls == 3:
                answer += 'Three bulls'
            elif bulls == 4:
                answer += 'You win!'

            print(answer)

        else:
            print('Guessed wrong!')
