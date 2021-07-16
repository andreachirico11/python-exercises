# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.
# Use the characters exactly once.


import random
letters = ['a', 'e', 'i', 'o', 'u']
words = []


# for l in letters:
#     other_ls = [let for let in letters if let != l]
#     created = ''
#     for l2 in other_ls:
#         created += l2
#     if not created in words:
#         words.append(created)


attempts = pow(len(letters), 3)

while len(words) != attempts:
    char_list = letters[:]
    random.shuffle(char_list)
    word = ''.join(char_list)
    if not word in words:
        words.append(word)

print(words)
