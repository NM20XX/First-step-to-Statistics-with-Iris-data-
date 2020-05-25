# histogram for each variables across species

# library used: matplotlib
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html

iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')


iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15,5))

params = {'legend.fontsize': 9, 'legend.handlelength': 1}
plt.rcParams.update(params)

ax1.hist(iris_setosa["sepal_length"], 
          color = 'darkcyan', label=names,alpha=0.5) 

ax2.hist(iris_virginica["sepal_length"] ,          
          color = 'darkmagenta', label=names,alpha=0.5) 

ax3.hist(iris_versicolor["sepal_length"],
          color = 'darkgreen', label=names,alpha=0.5) 


ax1.set_title("Iris setosa sepal length(cm)",fontsize=15)
ax2.set_title("Iris virginica sepal length(cm)",fontsize=15)
ax3.set_title("Iris versicolor sepal length(cm)",fontsize=15)

plt.tight_layout()
