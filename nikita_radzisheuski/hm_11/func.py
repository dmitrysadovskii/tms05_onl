from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def the_sum(self, a, b):
        pass

    @abstractmethod
    def the_difference(self, a, b):
        pass

    @abstractmethod
    def the_multiplication(self, a, b):
        pass

    @abstractmethod
    def the_dividing(self, a, b):
        pass
