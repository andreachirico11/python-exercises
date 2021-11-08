import itertools
import os

here = os.path.dirname(os.path.abspath(__file__))


# 1.1.1 Part 1
# Write a Python program to read first n lines of a file (you can use the test.txt file).
# HINT:use the islice(iterable, stop) function from the itertoolsmodule(check the documentation)
# in order to iterate on iterable up to stop times.

lines = []
n = 5

# with open(os.path.join(here, 'materials', 'test.txt'), 'r') as f:
#     for line in itertools.islice(f.readlines(), n):
#         lines.append(line)
# print(lines)


# 1.1.2 Part 2
# Write a Python program to append text to a file and display the whole text in the file.


# with open(os.path.join(here, 'materials', 'test.txt'), 'r+') as f:
#     f.writelines(['gianni'])
#     print(f.read())


# 1.1.3 Part 3
# Write a Python program to write a list to a file and prints the content when finished writing.

with open(os.path.join(here, 'materials', 'test.txt'), 'a+') as f:
    f.writelines(['gianni'])
    f.seek(-1)
    print(f.read())


# 1.1.4 Part 4
# Write a Python program to read a file line by line and store it into a list, then print the number of lines.
