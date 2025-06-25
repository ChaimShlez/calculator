from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle





class UI:
    def menu(self):
        isExit=True
        while  isExit:
            try:
                choice = int(input(
                    "\nChoose shape to calculate:\n"
                    "1: Calculate Circle\n"
                    "2: Calculate Square\n"
                    "3: Calculate Rectangle\n"
                    "4: Calculate Triangle\n"
                    "5: Calculate Hexagon\n"
                    "6: Exit\n"
                    "Enter your choice (1-6): "
                ))

                if not (1 <= choice <= 6):
                    print("Insert a number between 1 and 5")
                    continue

                match choice:
                    case 1:
                        self.calc_circle()
                    case 2:
                        self.calc_square()
                    case 3:
                        self.calc_rectangle()
                    case 4:
                        self.calc_triangle()
                    case 5:
                        self.calc_hexagon()
                    case 6:
                        print("good bay")
                        isExit=False


            except ValueError:
                print("Please enter a valid number.")

    def calc_circle(self):

        try:
            radius = float(input("Enter radius: "))
            self.validate(radius)
            self.createOb(Circle, radius)
        except ValueError as e:
            print(f"error - {e}")

    def calc_square(self):

        try:
            side = float(input("Enter side length: "))
            self.validate(side)
            self.createOb(Square, side)
        except ValueError as e:
            print(f"error -{e}")


    def calc_rectangle(self):

        try:
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            self.validate(width)
            self.validate(height)
            self.createOb(Rectangle, width, height)
        except ValueError as e:
            print(f"error -{e}")


    def calc_triangle(self):

        try:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            self.validate(base)
            self.validate(height)
            self.createOb(Triangle, base, height)
        except ValueError as e:
            print(f"error -{e}")


    def calc_hexagon(self):
        try:
            side = float(input("Enter side length: "))
            self.validate(side)
            self.createOb(Hexagon, side)
        except ValueError as e:
            print(f"error{e}")







    def createOb(self, shape_class, *args):
        shape = shape_class(*args)
        print(shape)
        print(f"Area: {shape.get_area()}")
        print(f"Perimeter: {shape.get_perimeter()}")
        print("------")

    def validate(self,num):
        if num <=0:
            raise ValueError(f"num invalid -{num}")


