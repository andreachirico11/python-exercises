# Given a 1D array, negate all elements which are between 3 and 8, in place.

import numpy

arr = numpy.arange(20)

print(arr)

arr[(arr > 3) & (arr < 8)] *= -1

print(arr)
