#################################
import sqlite3
from functools import reduce
import random
import string


def get_random_num(min, max):
    return random.randrange(min, max)


def get_random_string(length):
    return reduce(lambda acc, _: acc + string.ascii_lowercase[get_random_num(5, len(string.ascii_lowercase))], range(length), '')


def add_city_driver():
    lc = ['Roma', 'Milano', 'Firenze', 'Ancona']
    return random.choice(lc)


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS driver
                (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                  firstname VARCHAR(20),
                  lastname VARCHAR(30),
                  city VARCHAR(50),
                  age INTEGER,
                  n_cars INTEGER)""")


def add_driver(firstname, lastname, city, age, n_cars):
    data = (firstname, lastname, city, age, n_cars)
    c.execute(
        """INSERT INTO driver(firstname, lastname, city, age, n_cars) VALUES(?,?,?,?,?)""", data)


def create_driver():
    firstname = 'firstname_' + get_random_string(5)
    lastname = 'lastname_' + get_random_string(5)
    city = add_city_driver()
    age = get_random_num(18, 90)
    n_cars = get_random_num(1, 20)
    return (firstname, lastname, city, age, n_cars)


def add_drivers_to_db():
    drivers = tuple(create_driver() for _ in range(20))
    print(drivers)
    c.executemany(
        '''
      INSERT INTO driver(firstname, lastname, city, age, n_cars)
      VALUES (?,?,?,?,?)
      ''',
        drivers
    )


def get_driver():
    for row in c.execute("SELECT * FROM driver  ORDER BY lastname"):
        print(row)


def get_driver_most_cars():
    return c.execute("SELECT firstname, lastname,city, age, MAX(n_cars) FROM driver").fetchone()


def get_avg_city():
    return c.execute("SELECT city, AVG(age) FROM driver GROUP BY city").fetchall()


conn = sqlite3.connect('driver-sqlite.db')
c = conn.cursor()
create_table()
# add_drivers_to_db()
# add_city_driver()
# get_driver()
# print(get_driver_most_cars())
print(get_avg_city())
conn.commit()
conn.close()
################################################
