# Building up and breaking down features
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

customer_filepath = r"E:\Courses\Python Kaggle\Datasets\Customer Value Data\WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv"
customer_filepath = customer_filepath.replace("\\", "/")
customer = pd.read_csv(customer_filepath)

customer[['Type', 'Level']] = ( # Create Two new features
    customer['Policy']          # From the 'Policy' feature
    .str                        # Through the string accessor
    .split(" ", expand=True)    # by splitting on space " "
    
)                               # and expanding the result into separate columns
print(customer[['Policy', 'Type', 'Level']].head())

# Create a new feature by combining existing ones
autos_filepath = r"E:\Courses\Python Kaggle\Datasets\Automobile\Automobile_data.csv"
autos_filepath = autos_filepath.replace("\\", "/")
autos = pd.read_csv(autos_filepath)
print(autos.columns)
autos['make_and_style'] = autos['make'] + "_" + autos["body-style"]
print(autos[["make", "body-style", "make_and_style"]].head())