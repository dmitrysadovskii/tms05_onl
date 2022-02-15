from func import CalculatorMethods


class Calculator(CalculatorMethods):

    @staticmethod
    def is_valid(a, b):
        assert all(isinstance(number, (float, int)) for number in (a, b)), \
            "Вы ввели первое или второе число с другимм типом данных."

    def sum(self, a, b):
        self.is_valid(a, b)
        return print(f"Сумма чисел равна: {a + b}")

    def dif(self, a, b):
        self.is_valid(a, b)
        return print(f"Разность чисел равна: {a - b}")

    def mul(self, a, b):
        self.is_valid(a, b)
        return print(f"Произведение чисел равно: {a * b}")

    def div(self, a, b):
        self.is_valid(a, b)
        assert b != 0, 'Нельзя делить на 0'
        return print(f"Деление чисел равно:  {a / b}")
