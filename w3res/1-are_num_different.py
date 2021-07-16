# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other


def find_if_are_different(nums):
    s = set(list(nums))
    if len(s) == len(nums):
        return True
    return False


r = []

for i in range(100):
    r.append(i)

print(find_if_are_different(r))
print(find_if_are_different([1, 2, 3] + r))
