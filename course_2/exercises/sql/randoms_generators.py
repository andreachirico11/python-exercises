
from functools import reduce
import random
import string


def get_random_num(max):
    return random.randrange(1, max)


def get_random_string(length):
    return reduce(lambda acc, _: acc + string.ascii_lowercase[get_random_num(len(string.ascii_lowercase))], range(length), '')
