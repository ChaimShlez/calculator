from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle





class UI:

    def __init__(self):
        self.shapes=[]
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
                        self.createOb(Circle)
                    case 2:
                        self.createOb(Square)
                    case 3:
                        self.createOb(Rectangle)
                    case 4:
                        self.createOb(Triangle)
                    case 5:
                        self.createOb(Hexagon)
                    case 6:
                        print("goodbye")
                        isExit=False


            except ValueError:
                print("Please enter a valid number.")


    def createOb(self, shape):
        shape_config = {
            Circle: ["radius"],
            Square: ["side"],
            Rectangle: ["width", "height"],
            Triangle: ["base", "height"],
            Hexagon: ["side"]
        }

        param_names = shape_config.get(shape)

        params = []
        for name in param_names:
            value = float(input(f"Enter {name}: "))
            self.validate(value)
            params.append(value)

        shape = shape(*params)

        self.shapes.append(shape)
        print(shape)
        print(f"Area: {shape.get_area()}")
        print(f"Perimeter: {shape.get_perimeter()}")
        print("------")

    def validate(self,num):
        if num <=0:
            raise ValueError(f"num invalid -{num}")

