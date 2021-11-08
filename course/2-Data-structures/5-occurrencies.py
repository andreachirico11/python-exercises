
# 1) Write a program that asks the user for a sentence and prints out the number of occurrences of each word
# (in any order).
# Do not use class Counter.
# e.g.,: input “An apple is an apple”, prints an: 1, apple: 2, An: 1, is: 1
# 2) Do the same but considering case unsensitive words
# e.g.,: input “An apple is an apple”, prints an: 2, apple: 2, is: 1

phrase = 'An apple is an apple'
word_dic = {}

for word in phrase.split(' '):
    if word.lower() in word_dic:
        word_dic[word.lower()] += 1
    else:
        word_dic[word.lower()] = 1
print(word_dic)
