# importing modules

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

#Comparison between 4 numeric variables for each category.
params = {'legend.fontsize': 9
          , 'font.size': 16
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 16
          , 'xtick.labelsize': 14
          , 'ytick.labelsize': 14
          , 'figure.figsize' : (7,5)
         }
plt.rcParams.update(params)


iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

ax = sns.boxplot(data=iris_setosa, orient="v", palette="Set3").set_title("Iris setosa",fontsize=15)
plt.show()

ax = sns.boxplot(data=iris_virginica, orient="v",palette="Set3").set_title("Iris virginica",fontsize=15)
plt.show()

ax = sns.boxplot(data=iris_versicolor, orient="v",palette="Set3").set_title("Iris versicolor",fontsize=15)
plt.show()
