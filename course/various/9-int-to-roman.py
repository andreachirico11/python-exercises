# Int to Roman
# Solve the dual problem of 11.
# e.g.,
# Example 1: Input: 3 Output: “III”
# Example 2: Input: 4 Output: “IV”
# Example 3: Input: 9 Output: “IX”
# Example 4: Input: 58 Output: “LVIII” Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# Example 5: Input: 1994 Output: “MCMXCIV” Explanation: M = 1000, CM = 900, XC = 90 and
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


def get_all_combinations():
    letters = list(roman_numbers.keys())
    actual = ''
    actual_total = 0
    letter_i = 0
    counter = 1
    output = {}
    while True:
        if counter == 4:
            actual_total = -roman_numbers[letters[letter_i]]
            actual = letters[letter_i]
            letter_i += 1
        elif counter == 5:
            actual = ''
            actual_total = 0
        elif counter == 6:
            letter_i -= 1
        elif counter == 9:
            actual = letters[letter_i]
            actual_total = -roman_numbers[letters[letter_i]]
            letter_i += 2
        elif counter == 10:
            actual_total = 0
            actual = ''
            counter = 0
        actual += letters[letter_i]
        actual_total += roman_numbers[letters[letter_i]]
        counter += 1
        output[actual_total] = actual
        if actual_total == 1000:
            break
    return output


def split_num(num):
    output = []
    last_num = 0
    ten_remainder = 10
    while True:
        extracted = num % ten_remainder
        if last_num == extracted:
            break
        if ten_remainder == 10:
            output = [extracted]
        else:
            output = [extracted - last_num] + output
        ten_remainder *= 10
        last_num = extracted
    return output


def int_to_roman(int_num):
    roman_nums = [n for n in split_num(int_num)]
    all_combinations = get_all_combinations()
    output = ''
    for n in roman_nums:
        output += all_combinations[n]
    return output


print(int_to_roman(3))
print(int_to_roman(4))
print(int_to_roman(9))
print(int_to_roman(58))
print(int_to_roman(1994))
