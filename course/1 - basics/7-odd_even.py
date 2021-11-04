
# Write a program that asks the user for an integer n and prints: • n2 (its square) if n is odd, and
# • n/2ifniseven.
# Hint: use the integer reminder operator % (e.g., 5 % 2 == 1, 4 % 2 == 0)


numb = int(input('give the num: '))
print(numb/2 if numb % 2 == 0 else pow(numb, 2))
