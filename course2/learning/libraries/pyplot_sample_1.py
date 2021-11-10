import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, 0.2)
r = np.linspace(1,6, len(t))

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3,'^g')


plt.axis([0, 6, 0, 150])

plt.show()


