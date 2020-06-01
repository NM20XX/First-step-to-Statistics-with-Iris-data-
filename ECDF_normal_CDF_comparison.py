# load the iris data to a dataframe
iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

params = {'legend.fontsize': 15
          , 'font.size': 8
          , 'font.serif': ['Computer Modern Roman']
          , 'axes.labelsize': 16
          , 'xtick.labelsize': 15
          , 'ytick.labelsize': 15
         }
plt.rcParams.update(params)

iris_setosa = iris_data[iris_data['species'] == 'Iris-setosa']
iris_virginica = iris_data[iris_data['species'] == 'Iris-virginica']
iris_versicolor = iris_data[iris_data['species'] == 'Iris-versicolor']

# compute mean and standard deviation: mu, sigma
mu = iris_virginica["petal_length"].mean()
sigma = iris_virginica["petal_length"].std()

# Normal distribution with mean and std from iris_virginica["petal_length"] 
# 100000 sample
normal_theory = np.random.normal(mu,sigma,100000)

# Generate CDF
x_theor, y_theor = ecdf(normal_theory)

plt.plot(x_theor, y_theor,marker=  '.', linestyle='none')

#ECDF
x, y = ecdf(iris_virginica["petal_length"]) 

# Plot the CDFs and show the plot
ax = plt.plot(x_theor, y_theor, color = "b")
ax = plt.plot(x, y, marker='.', linestyle='none', color = "r")
ax = plt.xlabel('Values')
ax = plt.ylabel('CDF')
plt.title("Comparison between Normal CDF and ECDF of Iris virginica petal lengths",fontsize=15)

plt.show()
