import matplotlib.pyplot as plt
import seaborn
import pandas
import numpy

numpy.random.seed(2307)


mean = [0, 1]

cov = [[1, 0.5], [0.5, 1]]


data = numpy.random.multivariate_normal(
    mean,
    cov,
    200
)

df = pandas.DataFrame(
    data, columns=['x', 'y']
)

x = numpy.random.normal(size=100)

seaborn.jointplot(
    x='x',
    y='y',
    data=df
)

plt.show()
