from calculator import Calc
from rectangle import Rectangle


class Square(Rectangle):


    def __init__(self, width,):
        super().__init__(width, width)


    def get_area(self):

        return super().get_area()


    def get_perimeter(self):
        return super().get_perimeter()

    def __str__(self):
        return f"Square with side length {self._width}"


