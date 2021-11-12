from re import X
import matplotlib.pyplot as plt
from numpy.random.mtrand import seed
import seaborn
import pandas
import numpy

numpy.random.seed(2307)
seaborn.set_style('darkgrid')
tips = seaborn.load_dataset('tips')


# seaborn.regplot(
#     x='total_bill',
#     y='tip',
#     data=tips
# )

seaborn.lmplot(
    x='total_bill',
    y='tip',
    data=tips
)


plt.show()
