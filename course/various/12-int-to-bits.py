# 0.0.15 15. Int to Bits
# Write a program that ask the user for a positive integer number and prints out its bit representation as an array of 0 and 1.
# The conversion must be done “manually” (i.e., don’t use function bin() or other built-in functions).
# e.g.,
# input: 4, prints [1, 0, 0]
# input: 7, prints [1, 1, 1]
# input: 21, prints [1, 0, 1, 0, 1]

def int_to_bits(n):
    output = ''
    while True:
        if n % 2 == 0:
            output = '0' + output
        else:
            output = '1' + output
        if n == 1:
            break
        n = n // 2

    return output


print(int_to_bits(4))
print(int_to_bits(7))
print(int_to_bits(21))
