import math


def square_diff(a, b):
    return math.sqrt(a - b)


def odd_even(a, b):
    return True if a % 2 == 0 else False, True if b % 2 == 0 else False


def fact(n, actual=0):
    return actual if n == 0 else fact(n - 1, n if actual == 0 else actual * n)


__all__ = ['square_diff', 'odd_even']
