from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def sum(self, x: float, y: float):
        pass

    @abstractmethod
    def subtraction(self, x: float, y: float):
        pass

    @abstractmethod
    def multiplication(self, x: float, y: float):
        pass

    @abstractmethod
    def division(self, x: float, y: float):
        pass


class Calculator(Methods):

    def sum(self, first_number: float, second_number: float):
        return first_number + second_number

    def subtraction(self, first_number: float, second_number: float):
        return first_number - second_number

    def multiplication(self, first_number: float, second_number: float):
        return first_number * second_number

    def division(self, first_number: float, second_number: float):
        return first_number / second_number
