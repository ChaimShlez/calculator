from UI import UI
from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle

manu=UI()
manu.menu()
print(manu.shapes)
if len(manu.shapes)>1:
    for i in range(len(manu.shapes) - 1):
        shape1 = manu.shapes[i]
        shape2 = manu.shapes[i + 1]
        print(f"{shape1} + {shape2} = {shape1 + shape2}")


