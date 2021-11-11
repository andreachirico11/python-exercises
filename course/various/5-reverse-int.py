
# 0.0.7 7. Reverse Int
# Write a program that asks the user for an integer and print it out reversed.
# Assume that we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231−1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# You must work with integers, you cannot use convert it to string or use strings-related functions.
# e.g., input: “123”, prints 321 Input: “-123”, prints −321

num_range = (-231, 230)


def is_negative(n):
    if n < 0:
        return n * -1, -1
    return n, 1


def pow_ten(pow):
    if pow == 0:
        return 1
    output = 10
    for n in range(pow - 1):
        output *= 10
    return output


def remove_zeros(n):
    while True:
        if n < 10:
            break
        n = n // 10
    return n


def array_adder(prev_arr, num):
    if len(prev_arr) == 0:
        prev_arr.append(num)
        return prev_arr
    for n in prev_arr:
        num -= n
    prev_arr.append(remove_zeros(num))
    return prev_arr


def join_num_arr(arr):
    ten_exp = len(arr) - 1
    output = 0
    for n in arr:
        output += n * pow_ten(ten_exp)
        ten_exp -= 1
    return output


def reverser(n):
    rev_arr = []
    ten_exponent = 1
    abs_n, negative_mult = is_negative(n)
    while True:
        ten_multiplier = pow_ten(ten_exponent)
        num_to_add = abs_n % ten_multiplier
        ten_exponent += 1
        rev_arr = array_adder(rev_arr, num_to_add)
        if num_to_add == abs_n:
            break
    return join_num_arr(rev_arr) * negative_mult


print(reverser(123))
print(reverser(-123))
