# Model Validation
import pandas as pd
melbourne_filepath = r"E:\Courses\Python Kaggle\Datasets\melb_data.csv"
melbourne_filepath = melbourne_filepath.replace("\\","/")
melb_data = pd.read_csv(melbourne_filepath)
print(melb_data.describe()) # describing the dataset
print(melb_data.columns) # listing the columns in the dataset
melb_data = melb_data.dropna(axis=0) # dropping rows with missing values
print(melb_data.describe()) # describing the dataset after dropping missing values

# Choosing target variable and features
y = melb_data.Price  # Target variable we want to predict
melb_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']  # Features to help predict the price
x = melb_data[melb_features] # Selecting features from the dataset
print(x.describe())  # Describing the features
print(x.head())  # Displaying the first few rows of the features

from sklearn.tree import DecisionTreeRegressor
melb_model = DecisionTreeRegressor(random_state=1)  # Step 1: Defining the model type and setting random_state for reproducibility
melb_model.fit(x, y)  # Fitting the model to the data
from sklearn.metrics import mean_absolute_error
predicted_home_prices = melb_model.predict(x)  # Making predictions
mean_absolute_error(y, predicted_home_prices)  # Calculating the mean absolute error of the predictions
print("Mean Absolute Error:", mean_absolute_error(y, predicted_home_prices))  # Displaying the mean absolute error
print(melb_model.predict(x.head()))  # Predicting the price for the first 5 houses
print("Setup Complete") 