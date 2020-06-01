# Plot pairwise relationships in a dataset.

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

params = {'legend.fontsize': 15
          , 'font.size': 8
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 14
          , 'xtick.labelsize': 16
          , 'ytick.labelsize': 16
         }
plt.rcParams.update(params)

ax = sns.pairplot(iris_data,hue="species",diag_kind="hist", palette = 'husl')

plt.show()
