from func import Calculator_Methods


class Calculator(Calculator_Methods):

    @staticmethod
    def validation(x, y):
        try:
            value_1 = float(x)
            value_2 = float(y)
        except ValueError:
            raise TypeError("Invalid data type. Please, enter the numbers")

    def sum(self, x, y):
        try:
            self.validation(x, y)
            result = float(x) + float(y)
            print(f"The result is {result}")
        except Exception as error:
            print(error)

    def deduction(self, x, y):
        try:
            self.validation(x, y)
            result = float(x) - float(y)
            print(f"The result is {result}")
        except Exception as error:
            print(error)

    def multiplication(self, x, y):
        try:
            self.validation(x, y)
            result = float(x) * float(y)
            print(f"The result is {result}")
        except Exception as error:
            print(error)

    def division(self, x, y):
        try:
            self.validation(x, y)
            if float(y) == 0:
                raise ZeroDivisionError("Division by 0!")
            else:
                result = float(x) / float(y)
                print(f"The result is {result}")
        except Exception as error:
            print(error)


x = input("Enter value 1: ")
y = input("Enter value 2: ")
calculator = Calculator()
calculator.sum(x, y)
calculator.deduction(x, y)
calculator.multiplication(x, y)
calculator.division(x, y)
