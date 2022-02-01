import func


def validation(x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise TypeError(f"Invalid data type")


class Calculator(func.Methods):

    @staticmethod
    def sum(x, y):
        try:
            validation(x, y)
            result = float(x) + float(y)
            print(f"The result is {result}")
        except Exception as error:
            print(error)

    @staticmethod
    def deduction(x, y):
        try:
            validation(x, y)
            result = float(x) - float(y)
            print(f"The result is {result}")
        except Exception as error:
            print(error)

    @staticmethod
    def multiplication(x, y):
        try:
            validation(x, y)
            result = float(x) * float(y)
            print(f"The result is {result}")
        except Exception as error:
            print(error)

    @staticmethod
    def division(x, y):
        try:
            validation(x, y)
            if float(y) == 0:
                raise ZeroDivisionError(f"Division by 0!")
            else:
                result = float(x) / float(y)
                print(f"The result is {result}")
        except Exception as error:
            print(error)


x = input('Enter value 1: ')
y = input('Enter value 2: ')
calculator = Calculator()
calculator.sum(x, y)
calculator.deduction(x, y)
calculator.multiplication(x, y)
calculator.division(x, y)

calc = Calculator()
calc.sum(7, 0)
calc.deduction(7, 0)
calc.multiplication(7, 0)
calc.division(7, 0)
calc.multiplication('h', 'h')
calc.division(7, 7)
