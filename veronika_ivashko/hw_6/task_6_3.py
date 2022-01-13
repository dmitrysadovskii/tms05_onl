"""
3. Простейший калькулятор v0.1
Реализуйте программу, которая спрашивала у пользователя,
какую операцию он хочет произвести над числами,
а затем запрашивает два числа и выводит результат
Проверка деления на 0.

Пример
Выберите операцию:
    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление
Введите номер пункта меню:
>>> 4
Введите первое число:
>>> 10
Введите второе число:
>>> 3
Частное: 3, Остаток: 3
"""

operations = {
    1: 'Addition',
    2: 'Subtraction',
    3: 'Multiplication',
    4: 'Division'
}


def check_calc_input(user_number: str, verbose=True) -> bool:
    """
    Check if user entered valid number.
    :param user_number: some input from the user.
    :param verbose: to print feedback which numbers must be entered or not
    :return: bool - if user input was correct.
    """
    # minus_ascii = ord('-')  # 45
    # delimiter_ascii = ord('.')  # 46
    # zero_ascii = ord('0')  # 48
    # nine_ascii = ord('9')  # 57
    possible_codes = [i for i in range(ord('0'), ord('9') + 1)]
    possible_codes.extend([ord('-'), ord('.')])
    transformed_el = [ord(el) in possible_codes for el in user_number]
    if not all(transformed_el) or len(transformed_el) == 0:
        if verbose:
            print('Please enter only numbers: positive or negative.')
        return False
    else:
        return True


def make_calculations(num_of_operation: int, first_num: [float, int],
                      second_num: [float, int]) -> str:
    """
    Perform calculation with given numbers depending on number of operation.
    :param num_of_operation: key-number of operation required.
    :param first_num: first number for operation.
    :param second_num: second number for operation.
    :return: string describing input numbers, operation and result.
    """
    operation = operations.get(num_of_operation)
    if num_of_operation == 1:
        result = first_num + second_num
    elif num_of_operation == 2:
        result = first_num - second_num
    elif num_of_operation == 3:
        result = first_num * second_num
    else:
        if second_num != 0:
            whole_part = first_num // second_num
            precision = first_num % second_num
            result = f'integer from division is {whole_part} and ' \
                     f'remainder is {precision}'
        else:
            return 'Division by zero can not be performed'
    if num_of_operation != 4 and abs(result) == 0.0:
        result = 0
    return f'Result of {operation} between {first_num} and {second_num} is: ' \
           f'{result}'


def calculator_app() -> None:
    """
    Calculation application which asks user what operation of basic available
    (addition, subtraction, multiplication, division) he would like to
    perform, asks first and second number for operation,
    and prints the result.
    :return: None.
    """
    continue_calculation = True
    while continue_calculation:
        user_operation = input(f'Please select operation to perform: '
                               f'{operations}.\nType number of operation to '
                               f'proceed: ')
        if user_operation.isdigit() \
                and int(user_operation) in operations.keys():
            first_number = input('Please enter first number: ')
            # try to reenter valid first number
            while not check_calc_input(first_number):
                user_choice = input('Would you like to enter another first '
                                    'number or exit?\n'
                                    'Type y - to continue, n - to exit: ')
                if user_choice.lower() == 'n':
                    break
                else:
                    first_number = input('Please enter first number: ')
            # if first number is valid:
            if check_calc_input(first_number, verbose=False):
                second_number = input('Please enter second number: ')
                # try to reenter valid second number
                while not check_calc_input(second_number):
                    user_choice = input('Would you like to enter another '
                                        'second number or exit?\n'
                                        'Type y - to continue, n - to exit: ')
                    if user_choice.lower() == 'n':
                        break
                    else:
                        second_number = input('Please enter second number: ')
                if check_calc_input(second_number, verbose=False):
                    print(make_calculations(int(user_operation),
                                            float(first_number),
                                            float(second_number)))
        else:
            print('Please enter only number of selected operation')
        user_choice = input('Would you like to perform another operation?'
                            '\nType y - to continue, n - to exit: ')
        if user_choice.lower() == 'n':
            continue_calculation = False


calculator_app()
