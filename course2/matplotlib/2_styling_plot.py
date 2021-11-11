# Modify the plot so that:
# •the x-axis spans from 1 to 6, while the y-axis spans from 0 to 10
# • the first line has color green, dashed style, width 1 and diamond marker
# • the second line has color red, dotted style, width 2 and star marker
# •grid lines are yellow, dashed and have width 0.5
# The final result should be as sample 2:


import matplotlib.pyplot as plt


plt.axis([1, 6, 0, 10])
plt.title('Toy Plot')
plt.xlabel('x - axis')
plt.ylabel('y-axis')
plt.grid(color='y', linestyle='--', linewidth=0.5)

plt.plot([1, 2, 3, 4, 5], [2, 8, 1, 5, 6], 'g--D')

plt.plot([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 'r:*')

plt.legend(['first', 'second'])


plt.show()
