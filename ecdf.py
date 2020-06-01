# ecdf function

def ecdf(data):
    
    data_len = len(data)

    # ECDF X axis data
    # sorted order
    x = np.sort(data)

    # ECDF Y axis data
    y = np.arange(1, data_len + 1) / data_len

    return x, y

# You can run below line to see how the Y axis is getting generated
# print(np.arange(1, 150 + 1)/150)

##############################################################################

import matplotlib.pyplot as plt # library for creating visualizations
import seaborn as sns # library for making statistical graphics. Built on top of matplotlib
import statistics # calculating statistics of numeric data

# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

params = {'legend.fontsize': 11
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

# ECDF for petal_length of all species
x_set, y_set = ecdf(iris_setosa["petal_length"])
x_vers, y_vers = ecdf(iris_versicolor["petal_length"])
x_virg, y_virg = ecdf(iris_virginica["petal_length"])

plt.plot(x_set, y_set, marker='.', linestyle='none')
plt.plot(x_vers, y_vers, marker='.', linestyle='none')
plt.plot(x_virg, y_virg, marker='.', linestyle='none')

plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')

plt.title("Petal length ECDF comparison between species",fontsize=13)

ax = plt.xlabel('petal length (cm)')
ax = plt.ylabel('ECDF')

plt.show()
