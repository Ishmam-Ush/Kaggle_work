
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

sns.set_style("whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)
housing_filepath = r"E:\Courses\Python Kaggle\Datasets\California Housing\housing.csv"
housing_filepath = housing_filepath.replace("\\", "/")
df = pd.read_csv(housing_filepath)
print(df.columns)
X = df.loc[:, ["median_income", "latitude", "longitude"]]

# Create CLuster Feature
kmeans = KMeans(n_clusters=6)
X["Cluster"] = kmeans.fit_predict(X)
X["Cluster"] = X["Cluster"].astype("category")
print(X.head(10))

sns.relplot(
    x="longitude", y="latitude", hue="Cluster", data=X, height=6,
);
plt.show()

X["median_house_value"] = df["median_house_value"]
sns.catplot(x="median_house_value", y="Cluster", data = X, kind="boxen", height=6);
plt.show()
