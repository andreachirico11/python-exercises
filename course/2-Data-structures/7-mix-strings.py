
# Write a program that asks the user for two strings and prints the list of pairs composed by one letter of each string in order.
# If one of the strings is longer than the other, use symbol “?” for the missing letters of the shorter string.
# e.g.,
# • input “cat”, “dog” prints (‘c’, ‘d’), (‘a’, ‘o’), (‘t’, ‘g’)
# • input “cat”, “ocean” prints (‘c’, ‘o’), (‘a’, ‘c’), (‘t’, ‘e’), (‘?’, ‘a’), (‘?’, ‘n’) • input “stars”, “men” prints (‘s’, ‘m’), (‘t’, ‘e’), (‘a’, ‘n’), (‘r’, ‘?’), (‘s’, ‘?’)

short_word = 'cat'
long_word = 'ocean'
output = []

for i, letter in enumerate(list(long_word)):
    if len(short_word) > i:
        output.append((short_word[i], letter))
    else:
        output.append(('?', letter))

print(output)
