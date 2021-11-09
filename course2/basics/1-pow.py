# 1.1 Pow
# Write a program that asks the users two numbers a and b and
# prints ab without using operator **

def pw(base, esp):
    output = base
    for _ in range(esp - 1):
        output *= base
    return output


print(pw(2, 3))
