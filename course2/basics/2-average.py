# Write a program that asks the user for space-separated values (string or integers),
# it considers onlythe numbers and prints the average of them.
# e.g.,
# •
# input “10 8 9 9 0 6”, prints 7.0
# •
# input “hello world”, prints 0
# •
# input “10 hi 3”, prints 6.5
# Hint: use function
# is_digit
# to check if a string is a number


def average_nums(str):
    total = 0
    count = 0
    for char in str.split(' '):
        if char.isdigit():
            total += int(char)
            count += 1
    return 0 if total == 0 else total / count


print(average_nums('10 8 9 9 0 6'))
print(average_nums('hello world'))
print(average_nums('10 hi 3'))
