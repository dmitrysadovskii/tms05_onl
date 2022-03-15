from func import Methods


class Calculation(Methods):

    @staticmethod
    def validation(x, y):
        assert all(isinstance(number, int) for number in (x, y)), \
            "Numbers should be int-format"
        return True

    def addiction(self, x, y):
        self.validation(x, y)
        print(f"The result of addiction is {x + y}")

    def subtraction(self, x, y):
        self.validation(x, y)
        print(f"The result of subtraction is {x - y}")

    def multiplication(self, x, y):
        self.validation(x, y)
        print(f"The result of multiplication is {x * y}")

    def division(self, x, y):
        assert y != 0, 'y must not be 0'
        self.validation(x, y)
        print(f"The result of division is {x / y}")


calculate = Calculation()
calculate.addiction(1, 3)
calculate.division(90, 9)
calculate.multiplication(24, 6)
calculate.subtraction(6, 4)
