
# 0.0.14 14. Bits to Int
# Write a program that ask the user for a sequence of 0 and 1, a bit array, and prints out its integer value.
# Note that the input starts from the most significant bit.
# e.g.,
# input: “1 0 0 1 1 0”, prints 36
# input: “1”, prints 1
# input: “1 0 1 0 0”, prints 20


def bits_to_int_fn(bits):
    output = 0
    bits = bits.replace(' ', '')
    for i in range(len(bits)):
        output += pow(2, i) * int(bits[len(bits) - 1 - i])
    return output


# print(bits_to_int_fn("1 0 1 0 0"))
# print(bits_to_int_fn("1"))
# print(bits_to_int_fn("1 0 0 1 1 0"))
