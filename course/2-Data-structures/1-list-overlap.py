# Take two lists (you can use the ones in the example below) and
# write a program that prints a list that contains only the elements of
# the two lists that are equal and in the same position without duplication.

a = [5, 3, 5, 44, 4, 55, 4]
b = [5, 4, 55, 4, 4, 55, 4, 55, 9, 10, 11]
# prints 5 4 55
print([result for index, result in enumerate(a) if a[index] == b[index]])

print(set(b) & set(a))
