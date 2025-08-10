# Welcome to Feature Engineering , This is an introduction to feature engineering using a dataset from Kaggle.
# This code demonstrates how to create synthetic features from existing ones in a dataset.
# The dataset used is the Concrete Compressive Strength dataset from Kaggle.

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
# Load the dataset
concrete_filepath = r"E:\Courses\Python Kaggle\Datasets\Concrete\Concrete_Data.xls"
concrete_filepath = concrete_filepath.replace("\\", "/")
cd = pd.read_excel(concrete_filepath)
print(cd.head())
# Establishing a baseline score (good practice at the start of feature engineering)= helps decide if the new features are worth it
X = cd.copy()
print(repr(cd.columns[ -1 ]))
y = X.pop("Concrete compressive strength(MPa, megapascals)")
# Train and score baseline model
baseline = RandomForestRegressor(criterion="absolute_error", random_state=0)
baseline_score = cross_val_score(
    baseline, X , y , cv=5, scoring="neg_mean_absolute_error"
)
baseline_score = -1*baseline_score.mean()
print(f"MAE baseline_score:{baseline_score:.4}")

# Creating synthetic features
X["FCRatio"] = X["Fine Aggregate (component 7)(kg in a m^3 mixture)"]/ X["Coarse Aggregate  (component 6)(kg in a m^3 mixture)"]
X["AggCmtRatio"] = X["Coarse Aggregate  (component 6)(kg in a m^3 mixture)"] + X["Fine Aggregate (component 7)(kg in a m^3 mixture)"]
X["WtrCmtRatio"] = X["Water  (component 4)(kg in a m^3 mixture)"]/ X["Cement (component 1)(kg in a m^3 mixture)"]

# Train and score model with additional ratio features
model = RandomForestRegressor(criterion="absolute_error", random_state=0)
score = cross_val_score(
    model,X,y,cv=5 ,scoring="neg_mean_absolute_error"
)
score = -1*score.mean()
print(f"MAE with Ratio features:{score: .4}")
