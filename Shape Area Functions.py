import math
class Shapes:
    def __init__(self, shape_name, *args):
        self.shape = shape_name
        self.args = args

    def area(self):
        if self.shape == "rectangle":
            print(f"Area of Rectangle is {self.args[0] * self.args[1]}")
        elif self.shape == "circle":
            print(f"Area of Circle is {3.14 * (self.args[0] ** 2)}")
        elif self.shape == "triangle":
            print(f"Area of Triangle is {0.5 * self.args[0] * self.args[1]}")
        elif self.shape == "parallelogram":
            print(f"Area of Parallelogram is {self.args[0] * self.args[1]}")
        elif self.shape == "trapezoid":
            print(f"Area of Trapezoid is {0.5 * (self.args[0] + self.args[1]) * self.args[2]}")
        elif self.shape == "rhombus":
            print(f"Area of Rhombus is {self.args[0] * self.args[1]}")
        elif self.shape == "ellipse":
            print(f"Area of Ellipse is {3.14 * self.args[0] * self.args[1]}")
        elif self.shape == "polygon":
            print(f"Area of Regular Polygon is {(self.args[0] * self.args[1]) / 2}")
        elif self.shape == "sector":
            print(f"Area of Sector of a Circle is {(self.args[0]/360) * 3.14 * (self.args[1] ** 2)}")
        elif self.shape == "ring":
            print(f"Area of Ring is {3.14 * (self.args[0]**2 - self.args[1]**2)}")
        elif self.shape == "quadrilateral":
            print(f"Area of Quadrilateral is {0.5 * (self.args[0] * self.args[1]) * 3.14 * math.sin(self.args[2])}")
        elif self.shape == "square":
            print(f"Area of Square is {self.args[0] ** 2}")

# Values Below ||
#              \/

square = Shapes("square", 4)
triangle = Shapes("triangle", 5, 10)
ellipse = Shapes("ellipse", 3, 5)
polygon = Shapes("polygon", 6, 4)
ring = Shapes("ring", 8, 6)
rectangle = Shapes("rectangle", 5, 8)
circle = Shapes("circle", 3)
parallelogram = Shapes("parallelogram", 7, 10)
trapezoid = Shapes("trapezoid", 5, 8, 6)
rhombus = Shapes("rhombus", 4, 6)
circle_sector = Shapes("sector", 90, 5)
quadrilateral = Shapes("quadrilateral", 6, 8, 45)
#Calling Functions:
square.area()
triangle.area()
ellipse.area()
polygon.area()
ring.area()
rectangle.area()
circle.area()
parallelogram.area()
trapezoid.area()
rhombus.area()
circle_sector.area()
quadrilateral.area()