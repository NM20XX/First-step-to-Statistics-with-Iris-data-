# compute pairwise pearson correlation of variables, excluding NA/null value
import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

params = {'legend.fontsize': 15
          , 'font.size': 8
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 14
          , 'xtick.labelsize': 13
          , 'ytick.labelsize': 13
         }

plt.rcParams.update(params)
corrMatrix = iris_data.corr(method='pearson')
# heatmap of Correlation can help to identify the most correlated variables.
# look for values close to +1 and -1

sns.heatmap(corrMatrix, annot=True, cmap="Greens")
plt.xticks(rotation=45)
plt.show()
