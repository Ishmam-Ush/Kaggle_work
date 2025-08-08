import pandas as pd

# Loading the dataset
melb_filepath = r"E:\Courses\Python Kaggle\Datasets\melb_data.csv"
melb_filepath = melb_filepath.replace("\\", "/")

melb_data = pd.read_csv(melb_filepath, encoding = 'Latin1')
print(melb_data.describe())  # Describing the dataset
print(melb_data.columns)  # Listing the columns in the dataset
print("1st setup complete")
# Processing the dataset
melb_data = melb_data.dropna(axis=0)
print(melb_data.describe())  # Describing the dataset after dropping missing values
print("2nd setup complete")
y = melb_data.Price # Target variable we want to predict

melb_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude'] # Features to help predict the price
X = melb_data[melb_features] # Selecting features from the dataset
print(X.describe())  # Describing the features
print(X.head())  # Displaying the first few rows of the features
print("3rd setup complete")
from sklearn.model_selection import train_test_split
# Splitting the dataset into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state = 0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
# Defining the model
forest_model = RandomForestRegressor(random_state = 1)
forest_model.fit(train_X, train_y)  # Fitting the model to the training data
# Making predictions on the validation set
melb_predict = forest_model.predict(val_X)
# Calculating the mean absolute error on the validation set
print(mean_absolute_error(val_y, melb_predict))
