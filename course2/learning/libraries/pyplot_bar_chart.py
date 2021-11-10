import matplotlib.pyplot as plt
import numpy as np

data = [3.75, 4.75]
x_locations = np.random.normal(2,0.5,1000)
plt.hist(x, bins=10)


plt.bar(x_locations, data, width = 0.2)
plt.axis([0,2,0,5])
plt.title('wella')
plt.xticks(x_locations, ["label_1", "label_2"])


plt.show()


