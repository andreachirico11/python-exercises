# Subtract the mean of each row of a random matrix

import numpy
from functools import reduce

rand_m = numpy.random.rand(3, 3)

print(rand_m)

for row_index in range(len(rand_m)):
    rand_m[row_index] -= (reduce(lambda acc, current: acc +
                          current, rand_m[row_index]) / len(rand_m[row_index]))

print(rand_m)
