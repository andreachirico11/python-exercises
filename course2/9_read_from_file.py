# Given a names.txt file that has a list of a bunch of names,
# count how many of each name there are
# in the file, and print out the results to the screen


# with open('names.txt', 'x') as f:
#     f.close()

with open('names.txt', 'w') as f:
    f.writelines('gianni\npino\ngino\n')


with open('names.txt', 'r') as f:
    print(f.readlines())
