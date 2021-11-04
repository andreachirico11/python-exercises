# Write a program that asks the user for several numbers, one at a time, until the user writes “end”. The program then prints the sum of the input numbers.

summm = 0
while True:
    inp = input('give input: ')
    if inp == 'end':
        break
    summm += int(inp)

print(summm)
