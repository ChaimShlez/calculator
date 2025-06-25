from calculator import Calc
import math

from rectangle import Rectangle


class Triangle(Rectangle):

    def __init__(self, base, height):
        super().__init__(base, height)



    def get_area(self):

        return (self._width * self._height) /2

    def get_perimeter(self):
        third= math.sqrt(self._width**2 + self._height**2)
        return self._width + self._height + third


    def __str__(self):
     return f"Right Triangle with base {self._width} and height {self._height}"

    def __repr__(self):
        return self.__str__()





