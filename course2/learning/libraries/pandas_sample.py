import numpy
import pandas


r = 10
c = 4
data = numpy.random.rand(r,c)
columns = ['col_' + str(i+1) for i in range(c)]

df = pandas.DataFrame(data, columns = columns)
print(df)

url = "https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv"

dfp = pandas.read_csv(url)
print('-------------')
print(dfp.head())

print(dfp['salary'].values)

print(dfp.describe())

print(dfp.sample(5))

dfp_rank = dfp.groupby(['rank'])
print(dfp_rank.mean())

print(dfp.groupby(['sex']).mean())

df_ordered = dfp[dfp['sex'] == 'Female']
df_ordered.sort_values(by="salary")
print(df_ordered)

print(df[df.isnull().any(axis=1).head()])

