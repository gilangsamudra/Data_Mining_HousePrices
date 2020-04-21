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
# Bagian 2 - scatter plot
plot = plt.figure(dpi=150, figsize=(12, 6))
plt.scatter(df.eruptions, df.waiting)
plt.title('Old Faithful Data Scatterplot')
plt.xlabel('Leng of eruption (minutes)')
plt.ylabel('Time between eruptions (minutes)')
