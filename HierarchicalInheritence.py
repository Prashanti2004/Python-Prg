#Hierarchical Inheritence
class Shape:
    def area(self):
        print("Calculating area....")

class Circle(Shape):
    def area(self):
        print("Area of circle: pi*r*r")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle: length*breath")

circle = Circle()
rectangle = Rectangle()
circle.area()
rectangle.area()