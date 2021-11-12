import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

products = ['tooth_pick', 'nail_filer', 'rubber_stamp', 'floor', 'toy_top', 'clothes', 'computer', 'notebook', 'frying_pan', 'helmet',
            'marble', 'sponge', 'lemon', 'tea_pot', 'grid_paper', 'toy_car', 'pair_of_rubber_gloves', 'keyboard', 'lip_gloss', 'brush']

month = ['january', 'february', 'march', 'april', 'may', 'june',
         'july', 'august', 'september', 'october', 'november', 'december']


def get_random_num(min, max):
    return random.randrange(min, max)


def generate_sales(products_length):
    mat = []
    for _ in range(products_length):
        col = []
        for __ in range(12):
            col.append(get_random_num(1, 100))
        mat.append(col)
    return mat


df = pd.DataFrame(generate_sales(len(products)), index=products, columns=month)

print(df)

plt.axis([1, 12, 1, 100])


plt.xticks(range(1, 13), month)

plt.plot(df.values)
xlocations = [1.0, 6.0]
plt.legend(products)
plt.show()
