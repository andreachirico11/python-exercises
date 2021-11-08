# Take a list of numbers (bound it to a variable),
# and write a program that if the list consists of either odd or even outer pairs prints their sum;
# otherwise it prints “wrong input”.
# e.g.,
# • [1 2 5 10 3 10 7] -> outer pairs: (1,7), (2, 10), (5,3), (10, 10) => prints 48
# • [1 2 4 10 3 10 7] -> outer pairs: (1,7), (2, 10), (4,3), (10, 10) => prints “wrong input”

right = [1, 2, 5, 10, 3, 10, 7]
wrong = [1, 2, 4, 10, 3, 10, 7]

for i, n in enumerate(wrong):
    print(wrong[-i - 1])
    if n % 2 != wrong[-i - 1] % 2:
        print('wrong')
