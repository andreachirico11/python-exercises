# Write a function is_prime that, given an integer number,
# determines if the number is prime (re-turns True) or not (returns False).
# Let’s recall that a number is prime if it is not divisible by any of the numbers between 1 and itself.
# Advanced: write a function prime_numbers that, given an integer number n, returns the first n prime numbers.


from typing import Counter


def is_prime(n):
    return True if len([divisor for divisor in range(1, n + 1) if n % divisor == 0]) == 2 else False


print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
print(is_prime(10))
print(is_prime(11))
print(is_prime(12))
print('--------------------')


def prime_numbers(n):
    output = []
    possible_prime = 1
    count = 0
    while count < n:
        if is_prime(possible_prime):
            output += [possible_prime]
            count += 1
        possible_prime += 1
    return output


print(prime_numbers(20))
