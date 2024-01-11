import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (inputrad * inputrad)
        print("Area is: ", area)

    def perim(self):
        perim = math.pi * (inputrad * 2)
        print("Perimeter is: ", perim)


inputrad = int(input("Input radius: "))
sirkol = Circle(inputrad)

sirkol.area()
sirkol.perim()
