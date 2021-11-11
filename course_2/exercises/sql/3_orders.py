
# X Define a table that represents customers. The table contains an id, a customer name, the age of the customer and the gender.
# X Generate 100 random customers
# • Define a table that represents orders. The table contains an id and the cost of the order.
# . Customers and orders must be linked with a one-to-many relationship
# • Generate a random number (between 1 to 20) of random orders for each user
# • Write a function that takes an age and a gender and retrieves all the order issued by cus tomers of that gender with an age less or equal the age parameter.
# • Write a query that finds the top 10 customers by considering the sum of the cost of their orders
# • Write a query that computes the average age of the customers that issued at least 10 orders
# • Write a function that adds an order (a parameter of the function) to a user (the id of the user is a parameter of the function)
# • Write a function that deletes all the orders of a given user
# Modify the tables in a way that if a user is deleted all her/his orders are deleted too

# Solve the exercise with both plain sqlite3 and SQLAlchemy


import db_utils
from randoms_generators import get_random_num, get_random_string


db = db_utils.get_db_ref()
cursor = db.cursor()

genders = {
    'male': 'male',
    'female': 'female'
}


class Customer:
    def __init__(self, name, age, gender, _id=None) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self._id = _id
        self.as_object = {
            name: name,
            age: age,
            gender: gender
        }
        self.as_tuple = (
            name, age, gender
        )


def print_tuple(tup):
    for member in tup:
        print(member)


def create_t():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Customers(
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT
        )
        '''
    )


def empty_t():
    cursor.execute(
        '''
        DELETE FROM Customers
        '''
    )


def random_gender():
    return genders['male'] if get_random_num(10) % 2 == 0 else genders['female']


def generate_customer():
    return Customer(get_random_string(10), get_random_num(99), random_gender())


def generate_customers(n):
    return (generate_customer() for _ in range(n))


def add_customers(customers):
    cursor.executemany(
        '''
    INSERT INTO Customers(name, age, gender)
    VALUES (?,?,?)
    ''',
        map(lambda customer: customer.as_tuple, customers)
    )


# create_t()
# empty_t()
# add_customers(generate_customers(20))

db.commit()
db.close()
