# Create a program that asks for the user a string and prints “Yes” if it is palindrome “No” otherwise. e.g.,
# • input “anna” prints “Yes” • input “yes” prints “No”
# Hint: strings are arrays

phrase = input('give a phrase: ')
print('is palindrome' if "".join(list(phrase)[::-1])
      == phrase else 'is not palindrome')
