# Reverse a vector (first element becomes last).


import numpy
from utils import rand_nums

vec = numpy.array(rand_nums(20))
print(vec)
reversed_vec = vec[::-1]
print(reversed_vec)
