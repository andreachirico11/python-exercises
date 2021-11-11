# Create a 10x10 array with random values and find the minimum and maximum values

import numpy
arr = numpy.random.random(100).reshape(10, 10)
print(numpy.max(arr))
print(numpy.min(arr))
