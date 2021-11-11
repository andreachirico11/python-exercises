# Part 1
# Starting from the provided Dog class declaration, instantiate three new dogs, each with a different age.
# Then write a function called get_biggest_number(*args), that takes any number of ages (*args) and returns the oldest one.
# Then output the age of the oldest dog like so:
# The oldest dog is 7 years old.


class Dog:
    species = 'mammal'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False


class Runner():
    def __init__(self) -> None:
        self.name = 'Not Implemented'

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class RusselTerrier(Dog, Runner):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)


class Bulldog(Dog, Runner):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)


def get_biggest_number(*args):
    try:
        return max([dog.age for dog in args])
    except:
        return 'Not a dog'


terrier = RusselTerrier('pino', 3)
meticcio = Dog('boh', 9999)
bullo = Bulldog('caio', 1)

print(get_biggest_number(terrier, meticcio, bullo))


# Part 2
# Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class.
# In other words, the Dog class does not inherit from the Pets class.
# Then assign three dog instances to an instance of the Pets class. Your output should look like this:

# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they' re all mammals, of course.

class Pets:
    def __init__(self, *dogs) -> None:
        self.dogs = dogs

    def __str__(self) -> str:
        dogs = ''
        hungry_or_not = []
        for dog in self.dogs:
            dogs += (dog.name + ' is ' + str(dog.age) + '\n')
            hungry_or_not.append(dog.is_hungry)
        are_they_hungry = True in hungry_or_not
        return "\n\nI have 3 dogs.\n" + dogs + "And they' re all mammals, of course.\n" + "My dogs are{} hungry\n\n".format('' if are_they_hungry else ' not')

    def feed_all(self):
        for dog in self.dogs:
            dog.eat()


pets = Pets(terrier, meticcio, bullo)

print(pets)
pets.feed_all()
print(pets)


# Part 3
# Add an instance attribute is_hungry = True to the Dog class.
# Then add a method called eat() which changes the value of is_hungry to False when called.
# Feed all dogs and then print

# “My dogs are hungry.”
# if all dogs are hungry or
# “My dogs are not hungry.”
# if no dog is hungry.
# The final output should look like this:
# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.
# My dogs are not hungry.
