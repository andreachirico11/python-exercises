# Define a table that represents social-network posts.
# The table contains an id, a user id, the
# number of likes and the content.
# •Generate 10 random user_id and 1000 random posts for each user_id and add them to the
# database
# •Write a query to retrieve the post with more likes for each user
# •Write a function to retrieve the number of posts given a user_id
# •Write a function to retrieve the total number of likes given a user_id
# •Write a function that given a number N returns all the posts with a number of likes greater
# than N
# •Write a query that returns the top 10 users ranked by number of likes

import db_utils
from randoms_generators import get_random_num, get_random_string

db = db_utils.get_db_ref()
cursor = db.cursor()


def print_tuple(tup):
    for member in tup:
        print(member)


def create_t():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Posts(
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            likes INTEGER,
            content TEXT
        ) 
        '''
    )


def build_post(user_id):
    return (user_id, get_random_num(10), get_random_string(get_random_num(20)))


def empty_t():
    cursor.execute(
        '''
        DELETE FROM Posts
        '''
    )


def fill_t():
    user_ids = (lambda: tuple(range(1, 10)))()
    posts = [build_post(user_id)
             for user_id in user_ids for _ in range(100)]

    cursor.executemany(
        '''
        INSERT INTO Posts(user_id,likes, content)
        VALUES (?,?,?)
        ''',
        posts
    )


def get_the_post_with_more_likes_according_to_user():
    return cursor.execute(
        '''
        SELECT _id, user_id, MAX(likes)
        FROM Posts
        GROUP BY user_id

        '''
    ).fetchall()


def get_the_post_for_the_user(user_id):
    return cursor.execute(
        '''
        SELECT *
        FROM Posts
        WHERE user_id = ?

        ''',
        (user_id, )
    ).fetchall()


def get_total_likes_for_the_user(user_id):
    return cursor.execute(
        '''
        SELECT SUM(likes)
        FROM Posts
        WHERE user_id = ?

        ''',
        (user_id, )
    ).fetchall()[0]


def get_all_posts_with_likes_greater_than_N(n):
    return cursor.execute(
        '''
        SELECT *
        FROM Posts
        WHERE likes > ?

        ''',
        (n, )
    ).fetchall()


def get_top_10_users():
    return cursor.execute(
        '''
        SELECT DISTINCT user_id, likes
        FROM Posts
        ORDER BY likes DESC
        LIMIT 10
        '''
    ).fetchall()


# create_t()
# empty_t()
# fill_t()
# print(get_the_post_with_more_likes_according_to_user())
# print_tuple(get_the_post_for_the_user(3))
# print_tuple(get_total_likes_for_the_user(3))
# print_tuple(get_all_posts_with_likes_greater_than_N(3))
# print_tuple(get_top_10_users())

db.commit()
db.close()
