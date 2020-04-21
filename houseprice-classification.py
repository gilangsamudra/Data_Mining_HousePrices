# Bismillah
# Classification
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import sklearn
from sklearn import cluster

# Bagian 1 -  expolratory data analysis
df = pd.read_csv('D:/Phyton Code/Contoh dari Github/from-data-with-love-master/data/faithful.csv')
df.columns = ['eruptions', 'waiting']

# Bagian 2 - pandas scatter plot API
plot = plt.figure(dpi=150, figsize=(12, 6))
fig = plot.add_subplot()
fig.scatter(data=df, x='eruptions', y='waiting')
fig.set_title('Old Faithful Data Scatterplot')
fig.set_xlabel('Length of eruption (minutes)')
fig.set_ylabel('Time between eruptions (minutes)')
