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
sns.kdeplot(data=iris_data['Petal Length (cm)'], fill=True)
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

# Color coded plot
sns.histplot(data=iris_data, x="Petal Length (cm)", hue='Species')
plt.title("Histogram of Petal Lengths, by Species")
plt.xlabel('Petal Length (cm)')
plt.ylabel('Count')
plt.show()

# KDE plot for each species
sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', fill=True)
plt.title("Distribution of Petal Lengths,by Species")
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.show()

## Exercise
cancer_filepath = r"E:\Courses\Python Kaggle\Datasets\cancer.csv"
cancer_filepath = cancer_filepath.replace("\\", "/")
cancer_data = pd.read_csv(cancer_filepath, index_col='Id')
print(cancer_data.head(10))

print("max_perimeter = 87.46")
print("mean_radius = 9.504")
