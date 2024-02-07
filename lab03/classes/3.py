class Shape:
    def area(self):
        print("area equals to 0")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print("area equals to", self.width*self.length)

a = Rectangle(int(input()), int(input()))
b = Shape()

a.area()
b.area()