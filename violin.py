# violin plot 

# library used: seaborn
# https://seaborn.pydata.org/generated/seaborn.violinplot.html

iris_data = pd.read_csv('/kaggle/input/iris-flower-dataset/IRIS.csv')

ax = sns.violinplot(x="species", y="sepal_length", data=iris_data, palette="Set1")

