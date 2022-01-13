"""
1.Validate
Ваша задача написать программу, принимающее число - номер кредитной карты
(число может быть четным или не четным). И проверяющей может ли такая
карта существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
Примечания
    1. Алгоритм Луна
Примеры
validate(4561261212345464) #=> False
validate(4561261212345467) #=> True
"""


def check_user_input(user_number: str) -> bool:
    """
    Check if user entered any positive integer.
    :param user_number: some input from the user.
    :return: bool - if user input was correct.
    """
    if not user_number.isdigit():
        print('Be advised to enter only positive integer without any white '
              'spaces.')
        return False
    else:
        return True


def luhn_algorithm(card_number: str) -> bool:
    """
    Check if card number is valid, calculation depends on number of digits in
    card: last digit is a control one and is not used to check length of card
    number, if length of the string (without the last digit) is odd - adjust
    odd positional digits, even - adjust even positional digits. Adjustment
    logic: if digit*2 ia greater than 9 - subtract 9 from digit*2, else - leave
    digit*2, then calculate sum of adjusted and left numbers, if sum is
    multiple of 10 - card number is valid.
    :param card_number: sequence of digits as a string.
    :return: bool - is card number valid.
    """
    # split numbers by their position
    odd_numbers = [int(num) for num in card_number[::2]]
    even_numbers = [int(num) for num in card_number[1::2]]
    # for card with odd number of digits (don`t take into account last digit)
    if (len(card_number) - 1) % 2 != 0:
        numbers_to_calc, numbers_to_leave = odd_numbers, even_numbers
    else:
        numbers_to_calc, numbers_to_leave = even_numbers, odd_numbers
    adjusted_numbers = [(num * 2 - 9) if num * 2 > 9 else num * 2
                        for num in numbers_to_calc]
    # if sum of adjusted and left numbers is multiple of 10 > True
    return (sum(adjusted_numbers) + sum(numbers_to_leave)) % 10 == 0


def validate_app():
    """
    Main flow of Validate app which asks user to enter some card number, and
    returns the message - was card number valid or not due to Luhn algorythm.
    :return: None.
    """
    validation = {
        True: 'valid',
        False: 'invalid'
    }
    print('Welcome! Here you can check if your card number is valid.')
    continue_processing = True
    while continue_processing:
        user_card_number = input('Please enter card number to check: ')
        if check_user_input(user_card_number):
            result = luhn_algorithm(user_card_number)
            print(f'Provided card number is {validation.get(result)}.')
        user_choice = input('Would you like to make another try? '
                            'Type y - to continue / n - to exit: ')
        if user_choice.lower() == 'n':
            continue_processing = False
            print('Thanks for using our card service! Have a great day!')


validate_app()
