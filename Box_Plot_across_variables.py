# importing modules

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

# Box Plot for comparing all the numeric variables for each category:
params = {'legend.fontsize': 9
          , 'font.size': 16
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 16
          , 'xtick.labelsize': 15
          , 'ytick.labelsize': 17
         }
plt.rcParams.update(params)


iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,5))


ax = sns.boxplot(data=iris_setosa, orient="v", palette="husl", ax = ax1).set_title("iris_setosa",fontsize=20)
ax = sns.boxplot(data=iris_virginica, orient="v",palette="husl", ax = ax2).set_title("iris_virginica",fontsize=20)

fig, ax3 = plt.subplots(1,1,figsize=(10,5))
ax = sns.boxplot(data=iris_versicolor, orient="v",palette="husl", ax = ax3).set_title("iris_versicolor",fontsize=20)
