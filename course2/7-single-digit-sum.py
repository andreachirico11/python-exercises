# You are given two non-empty tuples representing two non-negative integers. Each element of the
# tuple is a digit of the integer, the first digit is the less significative. Write a function
# dsum()
# that
# adds up the two numbers and returns the result.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# You cannot convert the numbers in strings.
# Example
# Input: dsum((3, 4, 2), (4, 6, 5))
# Output: 807


def dsum(tup_1, tup_2):
    ten_multiplier = 1
    output = 0
    for i in range(len(tup_1) - 1, -1, -1):
        output += ((tup_1[i] + tup_2[i]) * ten_multiplier)
        ten_multiplier *= 10
    return output


print(dsum((3, 4, 2), (4, 6, 5)))
