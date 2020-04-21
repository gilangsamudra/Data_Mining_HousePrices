# Bismillah
# Clustering
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import cluster

# Bagian 1 -  expolratory data analysis
df = pd.read_csv('D:/Phyton Code/Contoh dari Github/from-data-with-love-master\
/data/faithful.csv')
df.columns = ['eruptions', 'waiting']

# Bagian 2 - pandas scatter plot API
plot = plt.figure(dpi=150, figsize=(12, 6))
fig = plot.add_subplot()
fig.scatter(data=df, x='eruptions', y='waiting')
fig.set_title('Old Faithful Data Scatterplot')
fig.set_xlabel('Length of eruption (minutes)')
fig.set_ylabel('Time between eruptions (minutes)')

# Bagian 3 - Clustering
dat = np.array(df)

# Bagian 4 -  K-means
k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(dat)

labels = kmeans.labels_
centroid = kmeans.cluster_centers_

# Bagian 5 - Visualization
for i in range(k):
    ds = dat[np.where(labels == i)]
    plt.plot(ds[:, 0], ds[:, 1], 'o', markersize=7)
    lines = plt.plot(centroid[i, 0], centroid[i, 1], 'kx')
    plt.setp(lines, ms=15, mew=4)
