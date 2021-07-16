# Given two integers N and K, the task is to find the Kth number which is not divisible by N.
# Note: The value of N is greater than 1, because every number is divisible by 1.


def kth_non_divisible(n, k):
    found_counter = 0
    divider = 1
    while True:
        if divider % n != 0:
            found_counter += 1
            if found_counter == k:
                return divider
        divider += 1


print(kth_non_divisible(3, 6))
print(kth_non_divisible(7, 97))
