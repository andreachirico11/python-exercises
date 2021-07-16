# 0.0.11 11. Roman to Int
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol Value
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000
# For example, two is written as II in Roman numeral, just two one’s added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90. C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Ask the user only numbers in range from 1 to 3999.
# e.g.,
# Example 1: Input: “III” Output: 3
# Example 2: Input: “IV” Output: 4
# Example 3: Input: “IX” Output: 9
# Example 4: Input: “LVIII” Output: 58 Explanation: C = 100, L = 50, XXX = 30 and III = 3
# Example 5: Input: “MCMXCIV” Output: 1994 Explanation: M = 1000, CM = 900, XC = 90 and
# IV = 4.

roman_numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def get_index(letter):
    return list(roman_numbers).index(letter)


def check_next_letter(actual_letter, next_letter):
    actual_index = get_index(actual_letter)
    next_index = get_index(next_letter)
    return actual_index + 1 == next_index or actual_index + 2 == next_index


def roman_to_int(roman_n):
    output = 0
    i = 0
    while i < len(roman_n):
        if i < len(roman_n)-1 and roman_n[i] == roman_n[i + 1]:
            if i < len(roman_n)-2 and roman_n[i] == roman_n[i + 2]:
                output += roman_numbers[roman_n[i + 2]]
                i += 1
            output += roman_numbers[roman_n[i]]
            output += roman_numbers[roman_n[i + 1]]
            i += 2
        else:
            if i < len(roman_n)-1 and check_next_letter(roman_n[i], roman_n[i + 1]):
                output += roman_numbers[roman_n[i + 1]]
                output -= roman_numbers[roman_n[i]]
                i += 1
            else:
                output += roman_numbers[roman_n[i]]
            i += 1
    return output


print(roman_to_int("III"))
print(roman_to_int("IV"))
print(roman_to_int("IX"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))


def roman_to_int_compact(roman_n):
    output = 0
    i = 0
    while i < len(roman_n):
        actual_value = roman_numbers[roman_n[i]]
        if i < len(roman_n) - 1:
            next_value = roman_numbers[roman_n[i + 1]]
            if actual_value < next_value:
                output += next_value - actual_value
                i += 2
                continue
        output += actual_value
        i += 1
    return output


print(roman_to_int_compact("III"))
print(roman_to_int_compact("IV"))
print(roman_to_int_compact("IX"))
print(roman_to_int_compact("LVIII"))
print(roman_to_int_compact("MCMXCIV"))
