import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(20)
y = np.random.rand(20)


print(x, y)

plt.scatter(x, y)

plt.show()


plt.savefig('grafico.png')
