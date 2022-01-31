import func


def is_int(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a и b могут быть только типа int")
    else:
        return True


class Calculator(func.Methods):

    def sum(self, a, b):
        valid = is_int(a, b)
        if valid:
            print(f"Сумма чисел равна: {a + b}")

    def dif(self, a, b):
        valid = is_int(a, b)
        if valid:
            print(f"Разность чисел равна: {a - b}")

    def mul(self, a, b):
        valid = is_int(a, b)
        if valid:
            print(f"Произведение чисел равно: {a * b}")

    def div(self, a, b):
        valid = is_int(a, b)
        if valid:
            try:
                print(f"Деление чисел равно:  {a / b}")
            except ZeroDivisionError:
                print("На ноль делить нельзя!!!")
