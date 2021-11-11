from math import pi

# Part 1
# Define a class with:
# •an attribute called s, which is initially an empty string
# and two methods:
# •getString: asks the user for an input string and stores the value in s;
# •printString: prints attribute s in upper case.
# Hints: - Use the input() function to ask for user input.


class FirstClass:
    def __init__(self) -> None:
        self.s = ''

    def getString(self, stri):
        self.s = stri

    def printString(self):
        return self.s.upper()


x = FirstClass()
x.getString('woo')
print(x.printString())


# Part 2
# Define a class with a class attribute called name.
# Hints: - The attribute value can be modified either directly or through the constructor.


class SecondClass:
    name = 'x'

    def __init__(self, x) -> None:
        self.x = x


# Part 3
# Define a class named Circle with a radius attribute.
# The Circle class must also provide a method to compute the area.
# Hints: - Use def methodName(self) to define a method.


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return 2 * pi * self.radius


print(Circle(10).get_area())


# Part 4
# Define a class Person and two child classes: Male and Female. All classes have a method
# “getGender” which prints “Male” for Male class and “Female” for Female class.
# Hints: - Use Subclass(Parentclass) to define a child class


class Person:
    def __init__(self, g=None) -> None:
        self.gender = g

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self, g=None) -> None:
        super().__init__(g='is a Male')


class Female(Person):
    def __init__(self, g=None) -> None:
        super().__init__(g='is a Female')


male = Male()
female = Female()
print(male.get_gender(), female.get_gender())
