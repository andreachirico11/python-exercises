# Write a function
# is_primethat, given an integer number, determines if the number is prime (re-turns True) or not (returns False).
# Let’s recall that a number is prime ifit is not divisible by any of the numbers between 1 and itself


def divisors(n):
    return [div for div in range(1, n+1) if n % div == 0]


def is_prim(n):
    return True if len(divisors(n)) == 2 else False


print(is_prim(2))
print(is_prim(3))
