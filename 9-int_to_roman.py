# # Int to Roman
# # Solve the dual problem of 11.
# # e.g.,
# # Example 1: Input: 3 Output: “III”
# # Example 2: Input: 4 Output: “IV”
# # Example 3: Input: 9 Output: “IX”
# # Example 4: Input: 58 Output: “LVIII” Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# # Example 5: Input: 1994 Output: “MCMXCIV” Explanation: M = 1000, CM = 900, XC = 90 and
# # IV = 4.

# roman_numbers = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }


# def reverse_dic(dic):
#     return {dic[key]: key for key in dic}


# numbers_roman = reverse_dic(roman_numbers)


# def split_num(num):
#     output = []
#     last_num = 0
#     ten_remainder = 10
#     while True:
#         extracted = num % ten_remainder
#         if last_num == extracted:
#             break
#         if ten_remainder == 10:
#             output = [extracted]
#         else:
#             output = [extracted - last_num] + output
#         ten_remainder *= 10
#         last_num = extracted
#     return output


# def ulterior_converter(lower, n, upper):
#     if abs(lower-n) > abs(upper-n):
#         # piu vicino a upper quindi 8 o 9
#         return 'boh'
#     else:
#         # 6 o 7
#         return 'middle'


# def roman_conv(n):
#     lower, upper = 0, 0
#     for key_n in numbers_roman:
#         if lower != 0 and upper != 0:
#             break
#         if key_n == n:
#             return numbers_roman[key_n]
#         elif key_n < n:
#             lower = key_n
#         elif key_n > n:
#             upper = key_n
#     return ulterior_converter(lower, n,  upper)


# print(roman_conv(900))


# def int_to_roman(int_num):
#     roman_nums = [n for n in split_num(int_num)]
#     return roman_nums


# # print(int_to_roman(3))
# # print(int_to_roman(4))
# # print(int_to_roman(9))
# # print(int_to_roman(58))
# # print(int_to_roman(1994))
