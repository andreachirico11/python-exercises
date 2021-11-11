
import os
import sqlite3


def generate_db_url():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exercises.db')


def get_db_ref():
    return sqlite3.connect(generate_db_url())
