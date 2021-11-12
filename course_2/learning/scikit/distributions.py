from re import X
import matplotlib.pyplot as plt
from pandas.core.algorithms import value_counts
import seaborn
import pandas
import numpy
from seaborn.distributions import kdeplot

numpy.random.seed(2307)
x = numpy.random.normal(size=100)

# seaborn.displot(
#     x)
# seaborn.displot(
#     x,
#     rug=True
# )
# seaborn.displot(
#     x,
#     rug=True,
#     kde=False
# )
seaborn.displot(
    x,
    bins=25
)


plt.show()
