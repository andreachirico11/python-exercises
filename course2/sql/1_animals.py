# •Define a table that represents animals. The table contains an id and the type of the animal
# (either cat, dog or bird).
# •Generate 1000 random animals
# •Write a query to retrieve the number of animals of each type
# •Write a query to retrieve the number of cats
# •Write a function that given a type of animal returns the count of that type


import db_utils
import random

db = db_utils.get_db_ref()
cursor = db.cursor()

animal_types = ('cat', 'dog', 'sheep')


class Animal:
    def __init__(self, type, id=None) -> None:
        self.type = type
        self.id = id

    def get_data(self):
        return (self.type, self.id)

    def get_data_without_id(self):
        return (self.type,)


def get_rand_type():
    return animal_types[random.randrange(0, 3)]


def gen_rand_animal():
    return Animal(get_rand_type()).get_data_without_id()


def gen_rand_animals(n):
    return [gen_rand_animal() for _ in range(n)]


def print_animals_per_type():
    cat, dog, sheep = map(lambda tup: tup[0], cursor.execute(
        '''
    SELECT COUNT(*)
    FROM Animals
    GROUP BY type
    ORDER BY type
    '''
    ).fetchall())
    print('cat: {}\ndog: {}\nsheep: {}\n'.format(cat, dog, sheep))


def create_t():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Animals(
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT
        ) 
        '''
    )


def empty_t():
    cursor.execute(
        '''
        DELETE FROM Animals
        '''
    )


def fill_t(animals_n):
    cursor.executemany(
        '''
        INSERT INTO Animals(type)
        VALUES (?)
        ''',
        gen_rand_animals(animals_n)
    )


def count_cats():
    print('\nThere are {} cats\n'.format(cursor.execute(
        '''
    SELECT COUNT(*)
    FROM Animals
    WHERE type='cat'
    '''
    ).fetchone()[0]))


def count_animal_of_type(anim_type):
    if anim_type not in animal_types:
        print('wrong')
    num_of_animals = cursor.execute(
        '''
            SELECT COUNT(*)
            FROM Animals
            WHERE type=?
            ''', (anim_type,)
    ).fetchone()[0],
    return '\nThere are {} {}s\n'.format(
        num_of_animals[0],
        anim_type
    )


create_t()
empty_t()
fill_t(20)
print_animals_per_type()
print(count_animal_of_type('cat'))
print(count_animal_of_type('dog'))


db.commit()
db.close()
