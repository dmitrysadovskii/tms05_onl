from abc import ABC
from abc import abstractmethod


class Calculator_Methods(ABC):

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
