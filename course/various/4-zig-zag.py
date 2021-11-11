
# 0.0.6 6. Zig Zag
# the string “PAYPALISHIRING” is written in a zigzag pattern on a given number of rows like this:
# P       A       H       N
#   A   P   L   S   I   I   G
#     Y       I       R
# And then read line by line: “PAHNAPLSIIGYIR”
# Write the code that will take a string s from the user and a number of row and make this conversion.
# e.g.,
# s = “PAYPALISHIRING”, num_rows = 3 prints “PAHNAPLSIIGYIR”
# s = “PAYPALISHIRING”, num_rows = 4 prints “PINALSIGYAHRPI”

def str_joiner(arr):
    output_str = ''
    for part in arr:
        output_str += part
    return output_str


def modify_output(newEl, output, rows, output_i):
    if len(output) < rows:
        output.append(newEl)
    else:
        output[output_i] += newEl
    return output


def check_incrementer(zig, rows, prev):
    if zig == rows-1:
        return -1
    elif zig == 0:
        return 1
    else:
        return prev


def zig_zag_converter(st, rows):
    output = []
    count = 0
    zig = 0
    incrementer = 1
    while count < len(st):
        output = modify_output(st[count], output, rows, zig)
        incrementer = check_incrementer(zig, rows, incrementer)
        zig += incrementer
        count += 1
    return str_joiner(output)


print(zig_zag_converter("PAYPALISHIRING", 3))
print(zig_zag_converter("PAYPALISHIRING", 4))
