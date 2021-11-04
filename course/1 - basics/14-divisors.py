# Create a program that asks the user for a number and then prints a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26/13 has no remainder.)

num_ref = int(input('num: '))
print([divisor for divisor in range(1, num_ref + 1) if num_ref % divisor == 0])
