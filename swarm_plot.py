# Swarm plot is a good complement to a box plot. 
# Here are they plotted together

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.swarmplot.html

# importing modules

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

params = {'legend.fontsize': 9
          , 'font.size': 16
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 16
          , 'xtick.labelsize': 17
          , 'ytick.labelsize': 14
         }
plt.rcParams.update(params)

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,5))

ax = sns.boxplot(x="species", y="sepal_length",data=iris_data, palette="Set3", ax = ax1).set_title("Sepal length across species",fontsize=17)
ax = sns.swarmplot(x="species", y="sepal_length", data=iris_data, color="purple", ax = ax1)

ax = sns.boxplot(x="species", y="sepal_width",data=iris_data, palette="Set3", ax = ax2).set_title("Sepal width across species",fontsize=17)
ax = sns.swarmplot(x="species", y="sepal_width", data=iris_data, color="purple", ax = ax2)


ax1.set_ylabel('')
ax1.set_xlabel('')

ax2.set_ylabel('')
ax2.set_xlabel('')

# Turn off tick labels
#ax1.set_yticklabels([])
#ax1.set_xticklabels([])

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,5))

ax = sns.boxplot(x="species", y="petal_length",data=iris_data, palette="Set3", ax = ax1,).set_title("Petal length across species",fontsize=17)
ax = sns.swarmplot(x="species", y="petal_length", data=iris_data, color="purple", ax = ax1)

ax = sns.boxplot(x="species", y="petal_width",data=iris_data, palette="Set3", ax = ax2).set_title("Petal width across species",fontsize=17)
ax = sns.swarmplot(x="species", y="petal_width", data=iris_data, color="purple", ax = ax2)

ax1.set_ylabel('')
ax1.set_xlabel('')

ax2.set_ylabel('')
ax2.set_xlabel('')

plt.show()
