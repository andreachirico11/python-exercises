# Write a program that asks the users for two words and prints True if the second is a permutation
# of the first otherwise prints False. The program should ignore the case of the letters.
# •
# input “spot”, “stop” prints True
# •
# input “cat”, “tac” prints True
# •
# input “hello”, “oleh” prints False (oleh has just one l instead of two)

def sorted(stri):
    copy = stri[:]
    return copy if copy.sort() else copy


def is_a_perm(str_1, str_2):
    return True if len(str_1) == len(str_2) and sorted(list(str_1)) == sorted(list(str_2)) else False


print(is_a_perm('spot', 'stop'))
print(is_a_perm('cat', 'tac'))
print(is_a_perm('hello', 'oleh'))
