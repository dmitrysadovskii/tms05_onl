"""Написать калькулятор. Программа должна содержать
4 функции принимающие два аргумента и возвращающие результаты
сложения, вычитания, умножения и деления. Реализовать
пользовательский интерфейс Methods. От него унаследовать
математические методы и реализовать их."""

import func


class Calculator(func.Methods):
    """Класс калькулятор, имеет 4 метода: для сложения,
    вычитания, умножения, деления. Каждый метод запрашивает
    у функции integer_check, являются ли введенные
    цифры целочисленными"""
    def the_sum(self, a, b):
        validation = integrer_check(a, b)
        if validation:
            print(f"Результат сложения: {a + b}")

    def the_difference(self, a, b):
        validation = integrer_check(a, b)
        if validation:
            print(f"Результат вычитания: {a - b}")

    def the_multiplication(self, a, b):
        validation = integrer_check(a, b)
        if validation:
            print(f"Результат умножения: {a * b}")

    def the_dividing(self, a, b):
        validation = integrer_check(a, b)
        if validation and b > 0:
            print(f"Результат деления:  {a / b}")
        else:
            print("Что-то пошло не так")


def integrer_check(a, b):
    """Обработка исключений. Если число а и число б целочисленные,
    функция возвращает True, тем самым позволяя выполняться функциям
    класса Калькулятор"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба числа должны быть целочисленными")
    else:
        return True
