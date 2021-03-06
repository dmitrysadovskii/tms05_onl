from abc import ABC, abstractmethod


class CalculatorMethods(ABC):

    @abstractmethod
    def sum(self, x, y):
        pass

    @abstractmethod
    def deduction(self, x, y):
        pass

    @abstractmethod
    def multiplication(self, x, y):
        pass

    @abstractmethod
    def division(self, x, y):
        pass
