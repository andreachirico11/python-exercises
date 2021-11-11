# 0.0.8 8. String to Int
# Write a program that takes a string in input from the user and it discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Assume that we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231−1], prints zero otherwise.
# Do not use the int() function.

# e.g.,
# 1. input: “42”, prints 42
# 2. input: ” -42”, prints -42
# Explanation: The first non-whitespace character is ‘-’, which is the minus sign. Then take as many numerical digits as possible, which gets 42.
# 3. input: “+4193 with words”, prints 4193
# Explanation: Conversion stops at digit ‘3’ as the next character is not a numerical digit.
# 4. input: “words and 987”, prints 0
# Explanation: The first non-whitespace character is ‘w’, which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
# 5. input: “-91283472332”, prints 0
# Explanation: The number “-91283472332” is out of the range of a 32-bit signed integer. Thefore 0 is returned.

def rem_first(st):
    return st[1:]


def remove_front_whitespace(string):
    while True:
        if string.startswith(' '):
            string = rem_first(string)
        else:
            break
    return string


def is_sign(sign):
    return sign == '-' or sign == '+'


def check_element_validity(sign):
    return is_sign(sign) or sign.isdigit()


def extract_str_num(string):
    output = ''
    for element in string:
        if check_element_validity(element):
            output += element
        else:
            break
    return output


def check_range(n_str, positive_range='231'):
    if is_sign(n_str[0]):
        n_str = rem_first(n_str)
    if len(n_str) < len(positive_range):
        return True
    return n_str < positive_range


def string_to_int(string):
    string = remove_front_whitespace(string)
    extracted_num = extract_str_num(string)
    if not check_element_validity(string[0]) or not check_range(extracted_num):
        return 0
    return extracted_num


print(string_to_int("   42"))
print(string_to_int("   43142"))
print(string_to_int("   000"))
print(string_to_int(" -42"))
print(string_to_int("+4193 with words"))
print(string_to_int(" words and 987"))
print(string_to_int(" words only"))
print(string_to_int("     -91283472332"))
