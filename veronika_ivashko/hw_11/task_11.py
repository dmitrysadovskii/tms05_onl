"""
Написать калькулятор.
Программа должна содержать 4 функции принимающие два аргумента и возвращающие
результаты сложения, вычитания, умножения и деления.

Реализовать пользовательский интерфейс Methods. От него унаследовать
математические методы и реализовать их.

Добавить валидацию входных данных.

Программа должна состоять из двух файлов(main.py, func.py).
"""
from func import CalculatorMathMethods, Validation, UserInteraction
calc = CalculatorMathMethods()
val = Validation()
ui = UserInteraction()


def get_valid_user_number() -> (str, bool):
    """
    Get from user some number, check it and if it is not a number, then ask
    user for another number until new number will be a valid one or user
    decides to quit.
    :return: valid user number as string or None.
    """
    number = ui.get_user_number()
    while not val.check_input_number(number):
        choice = ui.get_continue_permission('to enter another number')
        if choice.lower() == 'n':
            return
        else:
            number = ui.get_user_number()
    return number


def calculator_app():
    """
    Calculation application which asks user what operation of basic available
    (addition, subtraction, multiplication, division) he would like to
    perform, asks first and second number for operation,
    and prints the result.
    :return: None.
    """
    continue_calculation = True
    while continue_calculation:
        user_operation = ui.get_operation_number()
        if val.check_selected_operation(user_operation):
            x = get_valid_user_number()
            if x:
                y = get_valid_user_number()
                if y:
                    x, y = calc.to_number(x), calc.to_number(y)
                    math_operation = calc.get_function(user_operation)
                    result = math_operation(calc, x, y)
                    if result or result == 0:
                        ui.print_results(result, user_operation, x, y)
        to_continue = ui.get_continue_permission('to perform '
                                                 'another operation')
        if to_continue.lower() == 'n':
            continue_calculation = False


calculator_app()
