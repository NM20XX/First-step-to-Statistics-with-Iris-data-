# violin plot 

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.violinplot.html

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

ax = sns.violinplot(x="species", y="sepal_length", data=iris_data, palette="Set3")

plt.title("Sepal length violin plot",fontsize=16)

plt.xlabel('')
plt.ylabel('Sepal length in cm')
plt.show()
