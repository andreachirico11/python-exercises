# Create a program that asks the user for a sentence (i.e., space-separated words) and prints the word in the middle.
# e.g.,
# • input “What we think we become” prints “think” • input “His name is Adam” prints “name”
# Hint: if s is a string, you can use s.split() to split it into a list of words.

import math
sentence = input('sentence: ').split(' ')
print(sentence[math.ceil(len(sentence) / 2) - 1])
