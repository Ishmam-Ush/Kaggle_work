# Creating Features-->Group Transformations
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

customer["AverageIncome"] = (
    customer.groupby("State")  # Group by 'State'
    ["Income"]                 # select 'Income' column
    .transform("mean")         # calculate mean of 'Income' for each state
)
print(customer[["State", "Income", "AverageIncome"]].head(10))

customer["StateFreq"] = (
    customer.groupby("State")
    ["State"]
    .transform("count")
    / customer.State.count()
)

print(customer[["State", "StateFreq"]].head(10))

print(customer.columns)

# Create splits
df_train = customer.sample(frac=0.5)
df_valid = customer.drop(df_train.index)

# Create the average claim amount by coverage type, on the training set
df_train["AverageClaim"] = df_train.groupby("Coverage")["Total Claim Amount"].transform("mean")

# Merge the values into the validation set
df_valid = df_valid.merge(
    df_train[["Coverage", "AverageClaim"]].drop_duplicates(),
    on="Coverage",
    how="left",
)

print(df_valid[["Coverage", "Total Claim Amount", "AverageClaim"]].head(10))