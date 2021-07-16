# 0.0.9 9. Containers
# Given n non-negative integers a1, a2, …, an, where each represents a point at coordinate (i, ai). nvertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water (its area).
# Note: A container cannot be oblique, therefore you must use the minimum height of the two vertical lines.
# e.g.,
# Example 1: Input: [1, 1, 5, 4, 5, 6, 7, 2, 6] Output: 30
# Example 2: Input: [1, 1, 3, 4, 2] Output: 4
# Example 3: Input: [1, 2,3,4,5] Output: 6
c = 0


def get_height(h1, h2):
    if h1 > h2:
        return h2
    else:
        return h1


def find_max_water(heights):
    i = 0
    max = 0
    while i < len(heights):
        j = i + 1
        while j < len(heights):
            area = (j - i) * get_height(heights[i], heights[j])
            if area > max:
                max = area
            j += 1
        i += 1
    return max


print(find_max_water([1, 1, 5, 4, 5, 6, 7, 2, 6]))
print(find_max_water([1, 1, 3, 4, 2]))
print(find_max_water([1, 2, 3, 4, 5]))


# 0.0.10 10. Containers II
# Can you solve 9. by using a single loop?


def find_max_water_single(heights):
    i = 0
    j = len(heights) - 1
    output = 0
    while i < j:
        if heights[i] < heights[j]:
            output = max(output, (j-i) * heights[i])
            i += 1
        else:
            output = max(output, (j-i) * heights[j])
            j -= 1
    return output


print(find_max_water_single([1, 1, 5, 4, 5, 6, 7, 2, 6]))
print(find_max_water_single([1, 1, 3, 4, 2]))
print(find_max_water_single([1, 2, 3, 4, 5]))
