import numpy as np

x = np.array(range(0, 10))


print(x)

y = np.array([1, 2, 3], [3, 4])

z = np.concatenate((x, y), axis=0)


print(np.array([1, 2, 3, 4]).reshape(2, 2))
