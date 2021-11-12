from re import X
import matplotlib.pyplot as plt
from pandas.core.algorithms import value_counts
import seaborn
import pandas
import numpy

seaborn.set_style('darkgrid')

tips = seaborn.load_dataset('tips')

print(tips.head())


# SCATTERPLOT
seaborn.relplot(
    x='total_bill',
    y='tip',
    # hue='smoker',
    # style='time',
    data=tips,
    size='size'
)


# LINEPLOT

numpy.random.seed(2307)

df = pandas.DataFrame(
    dict(
        time=numpy.arange(500),
        value=numpy.random.rand(500).cumsum()
    )
)

seaborn.relplot(
    x='time',
    y='value',
    kind='line',
    data=df
)


####


fmri = seaborn.load_dataset('fmri')

seaborn.relplot(
    x='timepoint',
    y='signal',
    kind='line',
    ci='sd',  # confidence sd means standard deviation
    data=fmri,
    hue='event',
    # size='coherence'
)


df_2 = pandas.DataFrame(
    dict(
        time=pandas.date_range('2017-1-1', periods=500),
        value=numpy.random.rand(500).cumsum()
    )
)

g = seaborn.relplot(
    x='time',
    y='value',
    kind='line',
    data=df_2,
)

seaborn.relplot(
    x='timepoint',
    y='signal',
    hue='subject',
    col='region',
    row='event',
    kind='line',
    height=3,
    data=fmri
)


plt.show()
