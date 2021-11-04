# Write a program that asks the user for space-separated values (strings or integers), and prints the average of the numbers (discarding strings).
# e.g.,
# • input“1089906”prints7.0 • input “hello world” prints 0 • input “10 hi 3” prints 6.5
# Hint: use string method isdigit to check if a string is a number. E.g., if True if s represents a number, False otherwise.

inputs = input('give input: ').split()

summ = 0
for x in inputs:
    if x.isdigit():
        summ += int(x)
    else:
        summ = False
        break

print('strings' if summ is False else summ / (len(inputs) - 1))
