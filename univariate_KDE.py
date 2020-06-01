# bivariate density:

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html

# importing modules

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

params = {'legend.fontsize': 13
          , 'font.size': 8
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 14
          , 'xtick.labelsize': 12
          , 'ytick.labelsize': 12
         }
plt.rcParams.update(params)

iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

ax = sns.kdeplot(iris_virginica['petal_length'],shade=True, color = 'darkred')

plt.title("Iris virginica petal length univariate KDE plot",fontsize=14)

plt.xlabel('Petal length in cm')
plt.ylabel('Probability Density')
plt.show()
