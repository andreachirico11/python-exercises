'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. The
primenumbers.txt file has a list of all prime numbers under 1000, and the happynumbers.txt file
has a list of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes,
happy numbers are a real thing in mathematics -you can look it up on Wikipedia.
'''
import prime_num
from get_filename import get_filename

with open(get_filename('primenumbers'), 'w') as f:
    for n in range(1, 1000):
        if prime_num.is_prim(n):
            f.write(str(n) + '\n')


def split_num_in_digits(n):
    return [int(dig) for dig in list(str(n))]


def sum_powed_dig(digits):
    squared_sum = 0
    for digit in digits:
        squared_sum += (digit ** 2)
    return squared_sum


def is_happy(n):
    return sum_powed_dig(split_num_in_digits(sum_powed_dig(split_num_in_digits(n)))) == 1


with open(get_filename('happynumbers'), 'w') as f:
    for n in range(1, 1000):
        print(is_happy(n))
        if is_happy(n):
            f.write(str(n) + '\n')

common_nums = []
with open(get_filename('happynumbers'), 'r') as f_happy:
    with open(get_filename('primenumbers'), 'r') as f_primes:
        common_nums = [happy for happy in f_happy.readline()
                       if happy in f_primes.readlines()]

print(common_nums)
