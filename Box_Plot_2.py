# Box Plot 2:
# Here we are comparing across levels of a categorical variable

iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')


fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,5))

ax = sns.boxplot(x="species", y="sepal_length",data=iris_data, palette="Set3", ax = ax1).set_title("sepal_length across species",fontsize=20)
ax = sns.boxplot(x="species", y="sepal_width",data=iris_data, palette="Set3", ax = ax2).set_title("sepal_width across species",fontsize=20)


fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,5))

ax = sns.boxplot(x="species", y="petal_length",data=iris_data, palette="Set3", ax = ax1).set_title("petal_length across species",fontsize=20)
ax = sns.boxplot(x="species", y="petal_width",data=iris_data, palette="Set3", ax = ax2).set_title("petal_width across species",fontsize=20)
