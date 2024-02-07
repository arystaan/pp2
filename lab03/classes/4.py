import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print('(',self.x,',',self.y,')')
    
    def move(self, x_new, y_new):
        self.x = x_new
        self.y = y_new
    
    def dis(self, x2, y2):
        print('distance:', math.sqrt((x2 - self.x)**2 + (y2- self.y)**2))

point = Point(int(input("x coordinate:")), int(input("y coordinate:")))
print("coordinates are:")
point.show()
point.move(int(input("New x ccordinate:")), int(input("New y coordinate:")))
print("New coordinates:")
point.show()
point.dist(int(input("2nd point's x coordinate:")), int(input("2nd point's y coordinate:")))