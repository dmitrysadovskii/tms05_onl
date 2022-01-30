import func


def validation(x, y,):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x or y must be int")
    else:
        return True


class Calculator(func.Methods):

    def sum(self, x, y):
        valid = validation(x, y)
        if valid:
            result = x + y
            print(f"The result is {result}")

    def deduction(self, x, y):
        valid = validation(x, y)
        if valid:
            result = x - y
            print(f"The result is {result}")

    def multiplication(self, x, y):
        valid = validation(x, y,)
        if valid:
            result = x * y
            print(f"The result is {result}")

    def division(self, x, y):
        valid = validation(x, y)
        if valid:
            try:
                result = x / y
            except ZeroDivisionError:
                print("y = 0")
            else:
                print(f"The result is {result}")


calculator = Calculator()
calculator.sum(2, 3)
calculator.deduction(4, 4)
calculator.multiplication(0, 5)
calculator.division(5, 0)
