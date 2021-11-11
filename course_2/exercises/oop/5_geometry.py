# Part 1 - Shape
# Create a class representing a generic geometric shape.
# By means of two specific methods area() and perimeter(), the shape can return its area and perimeter.
# Since the shape is not specified yet, we want these methods to simply print the message “shape’s area”
# (respectively “shape’s perimeter”) and return the None value.

class Shape:
    def area(self):
        return None

    def perimeter(self):
        return None

# Part 2 - Square
# A Square is a Shape. It is characterized by its side, which is a required parameter when a square object is created.
# As a shape, a square returns its area and perimeter (which will have an actual value) by means of two specific methods
# (use the same names as in shape).


class Square(Shape):
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4

# Part 3 - Rectangle (1)
# A Rectangle is a Shape. It is characterized by two sides, which are required parameters when a rectangle object is created.
# As a shape, a rectangle returns its area and perimeter (which will have an actual value) by means of two specific methods
# (use the same names as inshape).

# Part 4 - Rectangle (2)
# We now want to be able to perform basic operations between rectangles.
# Define by means of operator overloading:
#     -string representation print “rectangle with sides: X,Y”
#     -comparison (one among “>” and “<” is enough): r1 > r2 if area(r1) is greater than area(r2)
#     -addition between rectangles (resulting in a rectangle whose longer side is the sum of the longer
#      sides and whose shorter side is the sum of the shorted sides)
#     -subtraction (works in the sameway)


class Rectangle(Shape):
    def __init__(self, base, height) -> None:
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return (self.base * 2) + (self.height * 2)

    def __str__(self) -> str:
        return "rectangle with sides: {},{}".format(self.base, self.height)

    def __it__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __add__(self, other):
        def get_shorter_side(rec):
            return rec.base if rec.base < rec.height else rec.height

        def get_longer_side(rec):
            return rec.base if rec.base > rec.height else rec.height
        return Rectangle(get_longer_side(self) + get_longer_side(other), get_shorter_side(self) + get_shorter_side(other))

    def __sub__(self, other):
        return self + other


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)

print(r1 - r2)

print('\n\n\n')


# Part 5 - Shapes
# Create a list of shapes containing a generic shape, a square, and a rectangle.
# Print it out by using the following code:
# for s in shapes:
# print(s.area())
# print(s.perimeter())
# print(s)

# Then, define a function printShape(n) that tries to print a single shape from the list without
# knowing about the list length (what happens if I writeprintShape(5)when the number of shapes is 3 ?).

shapes = [Rectangle(1, 2), Square(2), Shape()]


for s in shapes:
    print(s.area())
    print(s.perimeter())
    print(s)

print('\n\n\n')


def print_shape(n):
    try:
        print(shapes[n])
    except:
        print('index out of rangeeeee')


print_shape(452342)
print_shape(2)
