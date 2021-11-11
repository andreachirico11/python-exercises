import sqlite3
from get_filename import get_filename

url = get_filename('person').replace('txt', 'db')


def check_args(n, option, command):
    return len(command) == n and command[0] == option


def create_table():
    c.execute(
        '''
        CREATE TABLE persons
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            age INTEGER
        )
        '''
    )


def add_person(firstname, lastname, age):
    data = (firstname, lastname, age)
    c.execute(
        '''
        INSERT INTO persons(firstname, lastname, age)
        VALUES (?,?,?)

        ''', data
    )


def get_persons():
    for row in c.execute("SELECT * FROM persons ORDER BY lastname"):
        print(row)


def search_by_name(name):
    for row in c.execute("SELECT * FROM persons WHERE Firstname = ?", (name,)):
        print(row)


def main():
    stop = False
    while stop is not True:
        cmd = input(">>> ").split(' ')
        if check_args(1, '-create', cmd):
            create_table()
        elif check_args(4, '-add', cmd):
            add_person(cmd[1], cmd[2], cmd[3])
        elif check_args(1, '-show', cmd):
            get_persons()
        elif check_args(1, '-name', cmd):
            search_by_name(cmd[1])
        elif check_args(1, '-stop', cmd):
            stop = True
        else:
            print("invalid command")


MyDb = sqlite3.connect(url)
c = MyDb.cursor()

main()

MyDb.commit()
MyDb.close()
