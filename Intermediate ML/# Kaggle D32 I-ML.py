# XGBoost--> A technique to build and optimize models with gradient boosting
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
print(xgb.__version__) 
# Loading data
data = pd.read_csv(r"E:\Courses\Python Kaggle\Datasets\melb_data.csv")
# Predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
# Target
y = data.Price
# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

predictions = my_model.predict(X_valid)
print(f"Mean Absolute Error: {mean_absolute_error(predictions, y_valid)}")
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train)

my_model = XGBRegressor(n_estimators=500)
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train, 
            early_stopping_rounds=5, 
            eval_set=[(X_valid, y_valid)],
            verbose=False)
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(X_train, y_train, 
            early_stopping_rounds=5, 
            eval_set=[(X_valid, y_valid)], 
            verbose=False)

my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
my_model.fit(X_train, y_train, 
            early_stopping_rounds=5, 
            eval_set=[(X_valid, y_valid)], 
            verbose=False)
print(my_model.predict(X_valid))