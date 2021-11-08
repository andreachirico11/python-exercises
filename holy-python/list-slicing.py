wrd = "Toscana"


# Slice the word until first "a". (Tosc)
print(wrd[:4])

# Slice the word so that you get "cana".
print(wrd[3:])

# Now try to get "can" only.
print(wrd[3:-1])


# Can you slice the word from beginning to the end with steps of 2 (including the last character.)?
print(wrd[::2])


# Now slice the word with steps of 2, excluding first and last characters.
print(wrd[1:-1:2])


# Can you slice the list so that it's reversed without using the .reverse() method?
print(wrd[::-1])


# Slice the list so that only last 2 elements are included.
print(wrd[-2:])

# Slice the second and third elements (50 and 20) in the list.
lst = [40, 50, 20, 30, 90]
print(lst[1:3])
