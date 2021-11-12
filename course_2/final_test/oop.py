'''Write the definition of class Point. Objects from this class should have:
- an instance attribute for the point’s x-coordinate, and an instance attribute for the y-coordinate
- a method “show” to print the coordinates of the point
- a method “dist" that computes the distance between 2 points.
Write the code to test the “dist” method of Point. '''
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("x {} y{}".format(self.x, self.y))

    def dist(self, p):
        dx = (self.x - p.x)**2
        dy = (self.y - p.y)**2
        return math.sqrt(dx+dy)


p1 = Point(2, 2)
p2 = Point(4, 8)

p1.show()
p2.show()
p1.dist(p2)
