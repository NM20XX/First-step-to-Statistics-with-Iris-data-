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
          , 'xtick.labelsize': 15
          , 'ytick.labelsize': 15
         }
plt.rcParams.update(params)

iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

#species
names = ['iris_setosa', 'iris_virginica', 'iris_versicolor']

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15,5))


ax1.hist(iris_setosa["sepal_length"], 
          color = 'red', label=names, histtype = 'step') 

ax2.hist(iris_virginica["sepal_length"] ,          
          color = 'green', label=names,histtype = 'step') 

ax3.hist(iris_versicolor["sepal_length"],
          color = 'blue', label=names,histtype = 'step') 


ax1.set_title("Iris setosa sepal length",fontsize=18)
ax2.set_title("Iris virginica sepal length",fontsize=18)
ax3.set_title("Iris versicolor sepal length",fontsize=18)

# Set common labels
fig.text(0.0, 0.5,  'Frequency',  ha='center', va='center', rotation='vertical')
fig.text(0.5, 0.0, 'Sepal lenghts', ha='center', va='center', rotation='horizontal')

plt.tight_layout()
