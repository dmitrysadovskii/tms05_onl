"""
1. Быки и коровы
В классическом варианте игра рассчитана на двух игроков.
Каждый из игроков задумывает и записывает тайное 4-значное число
с неповторяющимися цифрами. Игрок, который начинает игру по жребию,
делает первую попытку отгадать число. Попытка — это 4-значное число
с неповторяющимися цифрами, сообщаемое противнику. Противник сообщает в ответ,
сколько цифр угадано без совпадения с их позициями в тайном числе
(то есть количество коров) и сколько угадано вплоть до позиции в тайном числе
(то есть количество быков).
При игре против компьютера игрок вводит комбинации одну за другой,
пока не отгадает всю последовательность.
Ваша задача реализовать программу, против которой можно сыграть в
"Быки и коровы"
Пример
Загадано число 3219
>>> 2310
Две коровы, один бык
>>> 3219
Вы выиграли!
"""
from random import choice


def get_computer_number() -> str:
    """
    Make up 4-digit number, which can not start from 0,
    and digits inside can not be repeated.
    :return: 4-digit number as string.
    """
    available_numbers = list(range(0, 10))
    computer_number = ''
    while len(computer_number) < 4:
        selected_number = choice(available_numbers)
        # to avoid 0 as first number
        while selected_number == 0 and len(computer_number) == 0:
            selected_number = choice(available_numbers)
        computer_number += str(selected_number)
        available_numbers.remove(selected_number)
    return computer_number


def check_user_input(number: str) -> bool:
    """
    Perform some validity checks on user`s input data:
    - only whole numbers, no floats,
    - 4-digit number not starting from zero,
    - only unique digits inside,
    - no text.
    :param number: some data entered by user.
    :return: 4-digit number as string.
    """
    if not number.isdigit():
        print('Please enter only whole numbers')
        return False
    elif len(number) != 4 or int(number) < 1000:
        print('Please enter non-null 4-digit number')
        return False
    elif len([i for i in number if number.count(i) == 1]) < 4:
        print('Please enter only unique numbers')
        return False
    else:
        return True


def count_cows(num_to_check: str, computer_number: str) -> int:
    """
    For each digit in num_to_check calculate number of occurrences
    in computer_number.
    :param num_to_check: number as string which must be checked.
    :param computer_number: number as string against which
    num_to_check will be verified.
    :return: number of digits found.
    """
    return sum([computer_number.count(num) for num in num_to_check])


def count_bulls(num_to_check: str, computer_number: str) -> int:
    """
    For each digit in num_to_check varify if there is the same digit at the
    same position in computer_number, if True, calculate number of such cases.
    :param num_to_check: number as string which must be checked.
    :param computer_number: number as string against which
    num_to_check will be verified.
    :return: number of occurrences found.
    """
    return sum([1 for i in range(len(num_to_check))
                if num_to_check[i] == computer_number[i]])


def play_cows_and_bulls() -> None:
    """
    Main flow of the game "Cows and Bulls" which uses other functions:
    - get_computer_number,
    - check_user_input,
    - count_cows,
    - count_bulls.
    :return: None
    """
    num_to_guess = get_computer_number()
    print('Let`s play "Cows and Bulls"!')

    continue_game = True
    while continue_game:
        user_number = input('Please, enter non_null 4-digit number for a guess'
                            ' (type "exit" to leave the game): ')
        if user_number.lower() == 'exit':
            print('Game is over')
            break
        else:
            print(f'User number: {user_number}')
            if check_user_input(user_number):
                bulls = count_bulls(user_number, num_to_guess)
                cows = count_cows(user_number, num_to_guess)
                if bulls == 4:
                    print('You win!')
                    print(f'Computer number: {num_to_guess}')
                    break
                else:
                    print(f'Number of cows is {cows}, '
                          f'number of bulls is {bulls}')


play_cows_and_bulls()
