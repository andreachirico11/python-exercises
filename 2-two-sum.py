
# 0.0.2 2. Two Sum
# Parse from the user an array of integers, and print the indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# e.g.,
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
# each input would have exactly one solution, and you may not use the same element twice.
# e.g.,
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

def two_summer(arr, target):
    output = []
    for n1 in arr:
        for n2 in arr:
            if n1 + n2 == target:
                output.append(n1)
                output.append(n2)
                break
        if len(output) == 2:
            break
    return output


print(two_summer([2, 7, 11, 15], target=9))


# 0.0.3 3. Two Sum (II)
# Can you solve 2. without using two nested loops?

def two_summer_rec(arr, target):
    if len(arr) > 2:
        middle = int(len(arr) / 2)
        output_1 = two_summer_rec(arr[0: middle + 1], target)
        if len(output_1) == 2:
            return output_1
        output_2 = two_summer_rec(arr[middle:], target)
        if len(output_2) == 2:
            return output_2
        return []
    else:
        if len(arr) == 2 and arr[0] + arr[1] == target:
            return arr
        return []


print(two_summer_rec([11, 13, 15, 2, 7], 9))
