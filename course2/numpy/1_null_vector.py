# Create a vector of size 10 in which all elements are 0’s except the fifth one, which is 1

import numpy

vec = numpy.array(
    list(map(lambda tup: 0 if tup[0] != 5 else 1, enumerate(range(10)))))

print(vec)
