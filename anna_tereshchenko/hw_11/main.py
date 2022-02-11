from func import Calculator

calc = Calculator()


def calculation(option, x, y):
    if option == 1:
        return print(f'Результат сложения = {calc.sum(x, y)}')
    elif option == 2:
        return print(f'Результат вычитания = {calc.subtraction(x, y)}')
    elif option == 3:
        return print(f'Результат умножения = {calc.multiplication(x, y)}')
    elif option == 4:
        return print(f'Результат деления = {calc.division(x, y)}')


def select_option():
    option = 0
    ask_number = True
    while ask_number:
        option = input('1. Сложение\n2. Вычитание\n3. Умножение\n'
                       '4. Деление\nВведите номер пункта меню:\n')
        if not option.isdigit():
            print('Это не число, пожалуйста, введите число')
            continue
        option = int(option)
        if not 1 <= option <= 4:
            print('Введите число от 1 до 4: ')
            continue
        ask_number = False
    return option


def select_numbers():
    ask_numbers = True
    first_number = ''
    second_number = ''
    while ask_numbers:
        first_number = input('Введите первое число: ')
        second_number = input('Введите второе число: ')
        is_valid_numbers = all(
            number.replace('.', '', 1).isdigit()
            for number in (first_number, second_number))
        if not is_valid_numbers:
            print('Вы ввели не числа')
            continue
        ask_numbers = False
    return float(first_number), float(second_number)


option = select_option()
first_number, second_number = select_numbers()
calculation(option, first_number, second_number)
