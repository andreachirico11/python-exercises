# Write a program that asks the user for two strings and prints the list of pairs composed by one
# letter of each string in order. If one of the strings is longer than the other,
# use symbol “?” for the missing letters of the shorter string.
# e.g.,
# •
# input “cat”, “dog” prints (‘c’, ‘d’), (‘a’, ‘o’), (‘t’, ‘g’)
# •
# input “cat”, “ocean” prints (‘c’, ‘o’), (‘a’, ‘c’), (‘t’, ‘e’), (‘?’, ‘a’), (‘?’, ‘n’)
# •
# input “stars”, “men” prints (‘s’, ‘m’), (‘t’, ‘e’), (‘a’, ‘n’), (‘r’, ‘?’), (‘s’, ‘?’)

def letter_or_question(st, position):
    return st[position] if len(st) > position else '?'


def mix_strings(str_1, str_2):
    return [(letter_or_question(str_1, i), (letter_or_question(str_2, i))) for i, _ in enumerate(str_1 if len(str_1) > len(str_2) else str_2)]


print(mix_strings('cat', 'dog'))
print(mix_strings('cat', 'ocean'))
