# Using matplotlib, draw a line plot as the one in the sample

import matplotlib.pyplot as plt


plt.axis([0.8, 5.2, 0.5, 8.5])
plt.title('Toy Plot')
plt.xlabel('x - axis')
plt.ylabel('y-axis')

plt.plot([1, 2, 3, 4, 5], [2, 8, 1, 5, 6], [5, 1], [1, 5])
plt.legend(['first', 'second'])

plt.show()
