# Swarm plot is a good complement to a box plot. 
# Here are they plotted together

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.swarmplot.html

iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,5))

ax = sns.boxplot(x="species", y="sepal_length", data=iris_data, palette="Set3", ax = ax1)
ax = sns.swarmplot(x="species", y="sepal_length", data=iris_data, color="purple", ax = ax1)

ax = sns.boxplot(x="species", y="sepal_width", data=iris_data, palette="Set3", ax = ax2)
ax = sns.swarmplot(x="species", y="sepal_width", data=iris_data, color="purple", ax = ax2)


fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,5))

ax = sns.boxplot(x="species", y="petal_length", data=iris_data, palette="Set3", ax = ax1)
ax = sns.swarmplot(x="species", y="petal_length", data=iris_data, color="purple", ax = ax1)

ax = sns.boxplot(x="species", y="petal_width", data=iris_data, palette="Set3", ax = ax2)
ax = sns.swarmplot(x="species", y="petal_width", data=iris_data, color="purple", ax = ax2)
