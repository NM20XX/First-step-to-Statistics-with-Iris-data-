# Box Plot 1:
# Here we are comparing between variables for each category

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.boxplot.html

iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')


iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(25,7))


ax = sns.boxplot(data=iris_setosa, orient="v", palette="Set3", ax = ax1).set_title("iris_setosa",fontsize=20)
ax = sns.boxplot(data=iris_virginica, orient="v",palette="Set3", ax = ax2).set_title("iris_virginica",fontsize=20)
ax = sns.boxplot(data=iris_versicolor, orient="v",palette="Set3", ax = ax3).set_title("iris_versicolor",fontsize=20)
