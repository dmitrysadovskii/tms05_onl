import func


def validate(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print('a or b is not int type')
    else:
        return True


class Calculator(func.Methods):

    def sum(self, a, b):
        val = validate(a, b)
        if val:
            print(f'The result is {a + b}')

    def diff(self, a, b):
        val = validate(a, b)
        if val:
            print(f'The difference of numbers is {a - b}')

    def mult(self, a, b):
        val = validate(a, b)
        if val:
            print(f'The multiplication result is {a * b}')

    def devision(self, a, b):
        val = validate(a, b)
        if val:
            if b != 0:
                print(f'The devision result is {a / b}')
            else:
                print('Сant divide by zero')


calculator = Calculator()
calculator.sum(10,2)
calculator.diff(9, 3)
calculator.mult(11, 2)
calculator.devision(120, 20)