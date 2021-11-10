# 1.5.1 Part 1
# Create a 8x8 matrix and fill it with a checkerboard pattern without using the tile function
# (Use thevalue 0 to represent white squares and 1 to represent the black squares).

import numpy

checkerboard = numpy.array(
    list(map(lambda tup: 0 if tup[0] % 2 == 0 else 1, enumerate(range(64))))).reshape(8, 8)


# 1.5.2 Part 2
# Create a checkerboard 8x8 matrix using the tile function (docs).

checkerboard = numpy.tile(numpy.array([0, 1]), 32).reshape(8, 8)
print(checkerboard)
