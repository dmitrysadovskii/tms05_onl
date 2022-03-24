"""HOMEWORK TASK NUMBER THREE
THIS CODE IS A SIMPLE CALCULATOR v0.1
"""

info_input = input('Простейший калькулятор v0.1\n'
                   'Справка - команда "faq"\n'
                   'Запуск калькулятора - команда "старт"\n'
                   'Ввод: ')


def my_calc():
    if info_input == 'faq':
        print('В простейшем калькуляторе v0.1 вы можете '
              'складывать, вычитать, умножать и делить числа.\n'
              'Для складывания введите: сложить.\n'
              'Для вычитания введите: вычесть.\n'
              'Для умножения введите: умножить.\n'
              'Для деления введите: разделить.\n')

    elif info_input == 'старт':
        operation_type = input('Что сделать: ')
        if operation_type == 'разделить':
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            if int(b) != 0:
                print(f"Результат деления: {int(a) / int(b)}")
            else:
                print('На ноль делить нельзя!')
        elif operation_type == 'умножить':
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            print(f"Результат умножения: {int(a) * int(b)}")
        elif operation_type == 'вычесть':
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            print(f"Результат вычетания: {int(a) - int(b)}")
        elif operation_type == 'сложить':
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            print(f"Результат сложения: {int(a) + int(b)}")
    else:
        print('OOPS! Something went wrong.')


my_calc()
