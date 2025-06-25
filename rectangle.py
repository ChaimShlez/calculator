from calculator import Calc


class Rectangle(Calc):



    def __init__(self,width,height):
        self._width=width
        self._height=height


    def get_area(self):
        return self._width* self._height


    def get_perimeter(self):
        return 2*self._height+ 2*self._width

    def __str__(self):
        return f"Rectangle with width {self._width} and height {self._height}"


    def __repr__(self):
        return self.__str__()