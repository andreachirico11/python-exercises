# NOT SOLVED


# 0.0.16 16. Kth Value
# Write a program that asks the user for two natural numbers X and K (K > 0).
# Print out the Kth number (starting from zero not included) number Y that satisfies:
# X + Y == X or Y
# e.g.,
# input: X = 10, K = 1, prints 1
# input: X = 10, K = 2, prints 4
# input: X = 10, K = 3, prints 5
# input: X = 17, K = 1, prints 2
# input: X = 17, K = 2, prints 4
# input: X = 17, K = 3, prints 6
# input: X = 17, K = 4, prints 8

def kth(x, k):
    found_counter = 0
    y = 0
    while True:
        if x + y == x or y:
            found_counter += 1
            if found_counter == k:
                return y
        y += 1


print(kth(10, 1))
print(kth(10, 2))
print(kth(10, 3))
print(kth(17, 1))
print(kth(17, 2))
print(kth(17, 3))
print(kth(17, 4))
