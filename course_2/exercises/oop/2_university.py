# Part 1 - Person
# Create a class that represents a person with a name, an age, and an address.
# The address is optional, and could be set after creation. The address is composed of a city,
# a state, and a residence string.
# Hints: - Attribute values are not limited to primitive types (e.g., strings, integers, boolean values...) but can be
# instances of a class as well.
# A person is able to execute an action called hello, that prints “Hello, I’m (name of the person)”

class Address:
    def __init__(self, city, state, residence):
        self.city = city
        self.state = state
        self.residence = residence


class Person:
    def __init__(self, name, age, address=None):
        self.name = name
        self.age = age
        self.address = address

    def hello(self):
        return "Hello, I'm {}".format(self.name)


p = Person('gianni', 3, Address('a', 'b', 'c'))

print(p.hello())


# Part 2 - Student
# Create a class that represents a student. A student is a person, but it is identified by a student code.
# A student is able to execute an action called hello, that prints:
#  “Hello, I’m (name of the person). My student code is (student code)”.
# If printed (with function print) a student object should print its student code.


class Student(Person):
    def __init__(self, name, age, st_code, address=None):
        super().__init__(name, age, address=address)
        self.code = st_code

    def hello(self):
        return "Hello, I'm {} and my code is {}".format(self.name, self.code)


st = Student('carlo', 3, 'sakdhflasjcnlac')

print(st.hello())


# Part 3 - Course
# Create a class that represents a university course. A course is identified by a name.
# If the course is started, students can enroll to it. By default a course is not started, but provides an action to begin.
# At any point one can display the enrolled students, by using this syntax:
# for i in range(0, len(course)):
# # course is a Course
# print(course[i])
# # prints an enrolled student’s name

class Course:
    def __init__(self, n) -> None:
        self.name = n
        self.is_started = False
        self.students = []

    def start_course(self):
        self.is_started = True

    def enroll(self, st_name):
        if self.is_started:
            self.students.append(st_name)

    def __len__(self):
        return len(self.students)

    def __getitem__(self, position):
        return self.students[position]


history = Course('history')
history.start_course()
history.enroll('gianni')
history.enroll('carlo')
history.enroll('pino')


def print_students(course):
    for i in range(0, len(course)):
        print(course[i])


print_students(history)
