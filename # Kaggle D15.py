import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

## Distribution
# Loading and examining the dataset
iris_filepath = r"E:\Courses\Python Kaggle\Datasets\iris.csv"
iris_filepath = iris_filepath.replace("\\","/")

iris_data = pd.read_csv(iris_filepath, index_col="Id")
print(iris_data.head(151))

# Histogram of the petal Length
sns.histplot(iris_data['Petal Length (cm)'])
print("Histogram of the Petal Length")
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Count")
plt.show()

# KDE plot of the petal Length
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
print("KDE plot of the Petal Length")
plt.title("KDE plot of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Density")
plt.show()

# 2D KDE plot of the petal Length and Width
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'],kind='kde')
print("2D KDE plot of Petal Length and Sepal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()

