from func import Methods_for_Calculator


class Calculator(Methods_for_Calculator):

    @staticmethod
    def validate(a, b):
        assert all(isinstance(number, int) for number in (a, b)),\
            "a or b must be int"
        return True

    def sum(self, a, b):
        self.validate(a, b)
        print(f'The result is {a + b}')

    def diff(self, a, b):
        self.validate(a, b)
        print(f'The difference of numbers is {a - b}')

    def mult(self, a, b):
        self.validate(a, b)
        print(f'The multiplication result is {a * b}')

    def devision(self, a, b):
        self.validate(a, b)
        if True:
            if b != 0:
                print(f'The devision result is {a / b}')
            else:
                print('Сant divide by zero')


calculator = Calculator()
calculator.sum(10, 2)
calculator.diff(9, 3)
calculator.mult(11, 2)
calculator.devision(120, 20)

