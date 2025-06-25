from abc import ABC,abstractmethod


class Calc(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass

    def __add__(self, other):
        # if not isinstance(other, Calc):
        #     return NotImplemented
        return self.get_area() + other.get_area()


