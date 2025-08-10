# FE S2 (Automobile Dataset)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")

df_filepath = r"E:\Courses\Python Kaggle\Datasets\Automobile\Automobile_data.csv"
df_filepath = df_filepath.replace("\\", "/")
df = pd.read_csv(df_filepath)
print(df.head())

X = df.copy()
X = X.replace("?", np.nan) # Replace '?' with NaN
X = X.dropna(axis=0, how="any") # Drop rows with any NaN values
X = X.reset_index(drop=True) # Reset index after dropping rows
y = X.pop("price")

# Label encoding for categorical features
for colname in X.select_dtypes("object"):
    X[colname], _ =X[colname].factorize()

# All discrete features should now have integer dtypes (have to double check before using MI)
discrete_features = X.dtypes == int

from sklearn.feature_selection import mutual_info_regression # Feature Engineering with Mutual Information
def make_mi_scores(X,y, discrete_features): # Function to calculate mutual information scores
    mi_scores = mutual_info_regression(X,y , discrete_features=discrete_features) # Calculate MI scores
    mi_scores = pd.Series(mi_scores, name= "MI Scores", index= X.columns) # Create a Series with MI scores
    mi_scores = mi_scores.sort_values(ascending=False) # Sort the scores in descending order
    return mi_scores
mi_scores = make_mi_scores(X,y, discrete_features)
print(mi_scores[::3]) # Display every third MI score for brevity

# Now a bar plot to make comparison easier
def plot_mi_scores(scores):
    scores = scores.sort_values(ascending= True) # Sort scores for plotting
    width = np.arange(len(scores)) # Create an array for bar widths
    ticks = list(scores.index) # Create a list of feature names for y-ticks
    plt.barh(width, scores) # Create horizontal bar plot
    plt.yticks(width,ticks) # Set y-ticks to feature names
    plt.title("Mutual Information Scores") # Set plot title
    
import numpy as np
df2 = df.replace('?', np.nan).copy()
df2['price'] = pd.to_numeric(df2['price'], errors='coerce')
df2['curb_weight'] = pd.to_numeric(df2['curb_weight'], errors='coerce')
df2 = df2.dropna(subset=['price','curb_weight'])

import seaborn as sns
sns.relplot(x='curb_weight', y='price', data=df2)   # now y is numeric


plt.figure(dpi=100, figsize=(8,5))
plot_mi_scores(mi_scores)
plt.show()
sns.relplot(x="curb-weight", y="price", data=df)
plt.show()
sns.lmplot(x="horsepower", y="price", hue="fuel-type", data=df)
plt.show()
