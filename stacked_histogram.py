# stacked histogram for each variables across species

# library used: matplotlib
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html

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
          , 'axes.labelsize': 16
          , 'xtick.labelsize': 12
          , 'ytick.labelsize': 12
         }
plt.rcParams.update(params)

iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

#species
colors = ['darkcyan', 'darkmagenta', 'cornflowerblue']
names = ['iris_setosa', 'iris_virginica', 'iris_versicolor']

plt.hist([iris_setosa["sepal_length"], iris_virginica["sepal_length"], 
          iris_versicolor["sepal_length"]],
          stacked=True, color = colors, label=names,alpha=0.5) 


# Plot formatting
plt.legend()
plt.title("Stacked histograms for sepal length",fontsize=15)

plt.xlabel('Sepal length in cm')
plt.ylabel('Frequency')

plt.tight_layout()
