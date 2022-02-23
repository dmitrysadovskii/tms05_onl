from abc import ABC, abstractmethod


class Methods_for_Calculator(ABC):

    @abstractmethod
    def sum(self, a, b):
        pass

    @abstractmethod
    def diff(self, a, b):
        pass

    @abstractmethod
    def mult(self, a, b):
        pass

    @abstractmethod
    def devision(self, a, b):
        pass
