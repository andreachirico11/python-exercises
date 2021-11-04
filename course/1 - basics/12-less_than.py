
# Write a program that asks the user for a list l of space-separated numbers, then asks for another number x and prints only the numbers in l that are less than x, without duplicates.
# e.g., input l = “2 5 19 4 2” and x = 5 prints 2 4.

num_ref = int(input('give reference: '))
num_list = [n2 for n2 in [
    int(n) for n in input('give numbers: ').split(' ')] if n2 < num_ref]
print(num_list)
