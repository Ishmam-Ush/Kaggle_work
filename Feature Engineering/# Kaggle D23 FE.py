# Creating Features
# We will learn number of common transformation we can do in pandas to create new features.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
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

accidents_filepath = (r"E:\Courses\Python Kaggle\Datasets\US traffic\US_Accidents_March23.csv")
accidents_filepath = accidents_filepath.replace("\\", "/")
accidents = pd.read_csv(accidents_filepath)

autos_filepath = r"E:\Courses\Python Kaggle\Datasets\Automobile\Automobile_data.csv"
autos_filepath = autos_filepath.replace("\\", "/")
autos = pd.read_csv(autos_filepath)

concrete_filepath = r"E:\Courses\Python Kaggle\Datasets\Concrete\Concrete_Data.xls"
concrete_filepath = concrete_filepath.replace("\\", "/")
concrete = pd.read_excel(concrete_filepath)

customer_filepath = r"E:\Courses\Python Kaggle\Datasets\Customer Value Data\WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv"
customer_filepath = customer_filepath.replace("\\", "/")
customer = pd.read_csv(customer_filepath)

# Creating Features
# Convert columns to numeric (non-convertible values become NaN)
autos["stroke"] = pd.to_numeric(autos["stroke"], errors="coerce")
autos["bore"] = pd.to_numeric(autos["bore"], errors="coerce")

autos["stroke-ratio"]= autos.stroke / autos.bore
autos[["stroke", "bore", "stroke-ratio"]].head()
print(autos[["stroke", "bore", "stroke-ratio"]].head())

# Map text numbers to integers
cylinder_map = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "eight": 8,
    "twelve": 12
}

# Replace text with numbers and convert to float
autos["num-of-cylinders"] = autos["num-of-cylinders"].replace(cylinder_map).astype(float)

autos["displacement"] = (
    np.pi * ((0.5 * autos.bore) ** 2) * autos.stroke * autos["num-of-cylinders"]
)
autos["displacement"].head()
print(autos["displacement"].head())

print(accidents.columns)

# If the feature has 0.0 values, use np.log1p (log(1+x)) instead of np.log
accidents["LogWindSpeed"] = accidents["Wind_Speed(mph)"].apply(np.log1p)

# Plot a comparison
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
sns.kdeplot(accidents["Wind_Speed(mph)"], shade=True, ax=axs[0])
sns.kdeplot(accidents.LogWindSpeed, shade=True, ax=axs[1]);
plt.show()


roadway_features = ["Amenity", "Bump", "Crossing", "Give_Way",
    "Junction", "No_Exit", "Railway", "Roundabout", "Station", "Stop",
    "Traffic_Calming", "Traffic_Signal"]
accidents["RoadwayFeatures"] = accidents[roadway_features].sum(axis=1)
accidents[roadway_features + ["RoadwayFeatures"]].head(10)
print(accidents[roadway_features + ["RoadwayFeatures"]].head(10))


