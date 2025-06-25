
import math

from circle import Circle



class Hexagon(Circle):

    def __init__(self,length):
       super().__init__(length)


    def get_area(self):
        return 3 * math.sqrt(3)*self._length**2/2

    def get_perimeter(self):
        return 6 * self._length

    def __str__(self):
        return f"Regular Hexagon with side length {self._length}"

    def __repr__(self):
        return self.__str__()

