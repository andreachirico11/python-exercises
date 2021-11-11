# empty class
class Emp:
    pass


class Student:
    def __init__(self, name, opt=0) -> None:
        self.name = name
        self.optional = opt


s1 = Student('gianni')


class Method_sample:
    def m1(self):
        print('we')

    def m2(self):
        pass


sample = Method_sample()

# print(sample.m1())


class Class_with_attrs:
    class_attr = 'we'

    def __init__(self, x) -> None:
        self.instance_attr = x


# print(Class_with_attrs.class_attr)


we_1 = Class_with_attrs(1)
we_2 = Class_with_attrs(2)

# print(we_1.class_attr, we_2.class_attr)

Class_with_attrs.class_attr = 'not we'

# print(we_1.class_attr, we_2.class_attr)


class With_class_methods:
    par = 0

    @classmethod
    def cls_met(cls):
        cls.par = 12
        pass


# print(With_class_methods.par)
With_class_methods.cls_met()
# print(With_class_methods.par)


class With_static_m:
    @staticmethod
    def st(a, b):
        return a + b

    def metodo(self, a, b):
        return self.st(a, b)


inst = With_static_m()
# print(inst.metodo(1, 2))


class Employee:
    def __init__(self, name, surname, company, age, salary) -> None:
        self.name = name
        self.surname = surname
        self.company = company
        self.age = age
        self.salary = salary

    def badge(self):
        print('{} wella wella'.format(self.name))


class Boss(Employee):
    def __init__(self, name, surname, company, age, salary, team) -> None:
        super().__init__(name, surname, company, age, salary)
        self.team = team


class Intern(Employee):
    def __init__(self, name, surname, company, age, boss_name) -> None:
        super().__init__(name, surname, company, age, 500)  # salary not assignable
        self.boss_name = boss_name


b = Boss('gianni', 'pino', 'gianniINC', 89, 1000000, 'belli')
intern_1 = Intern('paolo', 'paoli', 'gianniINC', 10, 'gianni')


# b.badge()
# intern_1.badge()


class Father:
    x = 1
    z = True

    def __init__(self, x, father_attr) -> None:
        self.common = x
        self.father_attr = father_attr


class Mother:
    y = 1
    z = False

    def __init__(self, x, mother_attr) -> None:
        self.common = x
        self.mother_attr = mother_attr


class Child(Father, Mother):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return 'overridee'

    def __add__(self, other):
        return 'add override    ' + str(other)

    def __getitem__(self, position):
        return 'muori'


c = Child('we', 'yo')
c2 = Child('wew', 'yoy')

# print(Child.z, c.common, c.father_attr, c.mother_attr)
# print(c + c2)

print(c[:])
