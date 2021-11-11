# Write a Python program to create and display a DataFrame from a specified dictionary data which
# has the index labels. Sample Python dictionary data and list labels:

import numpy as np
import pandas


exam_data = {
    'name': ['Luciano', 'Luca', 'Giovanni', 'Francesco', 'Riccardo', 'Eugenio', 'Danilo', 'Matteo', 'Marcello', 'Michele'],
    'score': [28, 29, 19, 15.5, 29, 30, 19, np.nan, 26, 7],
    'attempts': [1, 3, 2, 4, 2, 4, 1, 1, 3, 1]
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j']


data_frame = pandas.DataFrame(exam_data, columns=list(exam_data.keys()))


print('-----------')
print(data_frame.head())


# Display only the students that made more than 2 attempts
print('-----------')
print(data_frame[data_frame['attempts'] > 2].head())


# Write a Python program to sort the DataFrame first by score in descending order, then by name in ascending order
print('-----------')
print(data_frame.sort_values(by="score", ascending=False).head())


print('-----------')
print(data_frame.sort_values(by="name").head())
