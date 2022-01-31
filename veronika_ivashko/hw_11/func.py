from abc import ABC, abstractmethod


class AllMethods(ABC):

    @staticmethod
    @abstractmethod
    def addition(x, y):
        pass

    @staticmethod
    @abstractmethod
    def subtraction(x, y):
        pass

    @staticmethod
    @abstractmethod
    def division(x, y):
        pass

    @staticmethod
    @abstractmethod
    def multiplication(x, y):
        pass


class CalculatorMethods(AllMethods):

    @staticmethod
    def to_number(num: str) -> (float, int):
        """
        Cast from string integer number as integer, float number as float.
        :param num: already validated number as string.
        :return: float or integer nunmber.
        """
        if num.isdigit():
            return int(num)
        else:
            return float(num)

    @staticmethod
    def addition(x: (float, int), y: (float, int)) -> (float, int):
        return x + y

    @staticmethod
    def subtraction(x: (float, int), y: (float, int)) -> (float, int):
        return x - y

    @staticmethod
    def division(x: (float, int), y: (float, int)) -> (float, int):
        if y != 0:
            return x / y
        else:
            print(f'Division by zero is not supported.')

    @staticmethod
    def multiplication(x: (float, int), y: (float, int)) -> (float, int):
        return x * y

    @classmethod
    def perform_calculation(cls, key):
        """
        Call specific calculation method by the number which corresponds with
        math operations proposed to the user.
        :param key: number of operation.
        :return: callable function.
        """
        cal_methods = {
            '1': cls.addition,
            '2': cls.subtraction,
            '3': cls.multiplication,
            '4': cls.division
        }
        return cal_methods.get(key)


class Validation:
    operations = {
        '1': 'Addition',
        '2': 'Subtraction',
        '3': 'Multiplication',
        '4': 'Division'
    }

    @staticmethod
    def check_selected_operation(user_choice: str) -> bool:
        """
        Check if user selected available math operation.
        :param user_choice: input from user.
        :return: True if choice is available, None if not.
        """
        if user_choice.isdigit() \
                and user_choice in Validation.operations.keys():
            return True
        else:
            print(f'Only provided operations are available.')

    @staticmethod
    def check_input_number(user_number: str) -> bool:
        """
        Check if user provided valid input which can be converted into number.
        :param user_number: input from user.
        :return: True if input is valid, None if not.
        """
        try:
            float(user_number)
            return True
        except ValueError:
            print('Please, enter only positive or negative numbers.')


class UserInteraction:

    @staticmethod
    def get_operation_number() -> str:
        """
        Ask user to enter number of operation to perform.
        :return: user input as string.
        """
        return input(f'Please select operation to perform: '
                     f'{Validation.operations}.\nType number of operation to '
                     f'proceed: ')

    @staticmethod
    def get_user_number() -> str:
        """
        Ask user to enter some number to use in calculations.
        :return: user input as string.
        """
        return input('Please enter some number: ')

    @staticmethod
    def get_continue_permission(action_string) -> str:
        """
        Ask user if he would like to perform suggested actions.
        :param action_string: to do - action string to ask.
        :return: user input as string.
        """
        return input(f'Would you like {action_string}?'
                     f'\nType y - to continue, n - to exit: ')

    @staticmethod
    def print_results(result, operation_num, x, y):
        """
        Provide (print) results of the calculation to the user.
        :param result: number.
        :param operation_num: number of operation chosen.
        :param x: first number.
        :param y: second number.
        :return: None.
        """
        operation = Validation.operations.get(operation_num)
        print(f'Result of {operation} between {x} and {y} is equal to '
              f'{result}.')
