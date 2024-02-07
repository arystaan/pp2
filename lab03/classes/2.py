class Shape:
    def area(self):
        print("Area equals to 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Area equals to", self.length ** 2)

a = Square(int(input()))

b = Shape()

a.area()
b.area()
