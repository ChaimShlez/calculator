from calculator import Calc
import math

class Circle(Calc):



    def __init__(self, length):
        self._length = length

    def get_area(self):
        return math.pi * self._length ** 2


    def get_perimeter(self):
        return 2 * math.pi * self._length

    def __str__(self):
        return f"Circle with radius {self._length}"

    def __repr__(self):
        return self.__str__()
