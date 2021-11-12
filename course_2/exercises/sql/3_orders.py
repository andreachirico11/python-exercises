
# X Define a table that represents customers. The table contains an id, a customer name, the age of the customer and the gender.
# X Generate 100 random customers
# X Define a table that represents orders. The table contains an id and the cost of the order.
# X Customers and orders must be linked with a one-to-many relationship
# X Generate a random number (between 1 to 20) of random orders for each user
# X Write a function that takes an age and a gender and retrieves all the order issued by
#   customers of that gender with an age less or equal the age parameter.
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


# class Customer:
#     def __init__(self, cost, _id=None, customer_id=None) -> None:
#         self.cost = cost
#         self._id = _id
#         self.as_tuple = (
#             cost, customer_id
#         )


class Shop_Order:
    def __init__(self, cost, customer_id, _id=None) -> None:
        self._id = _id
        self.cost = cost
        self.customer_id = customer_id
        self.as_tuple = (
            cost, customer_id
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


def create_order_t():
    cursor.execute(
        '''
    CREATE TABLE IF NOT EXISTS Shop_Orders(
        _id INTEGER PRIMARY KEY AUTOINCREMENT,
        cost INTEGER,
        customer_id INTEGER,
        CONSTRAINT fk FOREIGN KEY(customer_id) REFERENCES Customers(_id)
        ON DELETE CASCADE
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


def generate_order(cust_id):
    return Shop_Order(get_random_num(100), cust_id).as_tuple


def generator(n, cust_id=None):
    return tuple(generate_customer() if not cust_id else generate_order(cust_id) for _ in range(n))


def generate_orders_for_customers(customer_ids):
    orders_by_user = tuple(
        map(lambda cust_id: generator(10, cust_id), customer_ids))
    list_of_orders = []
    for order_of_a_user in orders_by_user:
        for order in order_of_a_user:
            list_of_orders.append(order)
    return tuple(list_of_orders)


def add_customers(customers):
    cursor.executemany(
        '''
    INSERT INTO Customers(name, age, gender)
    VALUES (?,?,?)
    ''',
        map(lambda customer: customer.as_tuple, customers)
    )


def get_customer_ids():
    return map(lambda tup: tup[0], cursor.execute(
        '''
        SELECT _id
        FROM Customers
        '''
    ))


def add_orders(orders):
    cursor.executemany(
        '''
    INSERT INTO Shop_Orders(cost, customer_id)
    VALUES (?,?)
    ''',
        orders
    )


def get_orders_by_filtered_customer(age, gender):
    return cursor.execute(
        '''
        SELECT *
        FROM Shop_Orders
        WHERE customer_id in (
            SELECT _id
            FROM Customers
            WHERE gender = ? AND age <= ?
        )
        ''', (gender, age)
    )


def get_top_10_customers():
    return cursor.execute(
        '''
        SELECT *
        FROM Customers as c JOIN Shop_Orders as s ON c._id = s.customer_id
        WHERE
        '''
    )


# create_t()
# empty_t()
# add_customers(generate_customers(20))
# create_order_t()
# print_tuple(get_customer_ids())
# add_orders(generate_orders_for_customers(get_customer_ids()))
# print_tuple(get_orders_by_filtered_customer(20, genders['female']))
print_tuple(get_top_10_customers())

db.commit()
db.close()
