# Testing Dataset practice sheet
import pandas as pd
# Loading the dataset
car_sale_filepath = r"E:\Courses\Python Kaggle\Datasets\Car sales\Cars Datasets 2025.csv"
car_sale = car_sale_filepath.replace("\\","/")
car_data = pd.read_csv(car_sale, encoding='Latin1')
print(car_data.describe()) # Describing the dataset
car_data.columns= car_data.columns.str.replace(' ', '_') # Replacing spaces in column names with underscores
print(car_data.columns) # Listing the columns in the dataset
print("1st setup complete")
# processing the dataset
car_data = car_data.dropna(axis=0) # Dropping rows with missing values
print(car_data.describe()) # Describing the dataset after dropping missing values
print("2nd setup complete")
# Choosing target variable and features
y = car_data.Cars_Prices # Target variable we want to predict
car_features = ['CC/Battery_Capacity','HorsePower','Total_Speed','Performance(0_-_100_)KM/H','Fuel_Types','Seats','Torque']  # Features to help predict the price 
X = car_data[car_features] # Selecting features from the dataset
print(X.describe())  # Describing the features
print(X.head())  # Displaying the first few rows of the features

from sklearn.tree import DecisionTreeRegressor
car_model = DecisionTreeRegressor(random_state=1) # Step 1: Defining the model type and setting random_state for reproducibility
car_model.fit(X,y)
from sklearn.metrics import mean_absolute_error
predicted_car_prices = car_model.predict(X)  # Making predictions
mean_absolute_error(y, predicted_car_prices)  # Calculating the mean absolute error of the predictions
print("Mean Absolute Error:", mean_absolute_error(y, predicted_car_prices))  # Displaying the mean absolute error
print(car_model.predict(X.head()))  # Predicting the price for the first 5 cars
print("Setup Complete")

from sklearn.model_selection import train_test_split
# Splitting the dataset into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=1)
# Defining the model again for the training set
car_model = DecisionTreeRegressor(random_state=1)
# Fitting the model to the training data
car_model.fit(train_X, train_y)
# Making predictions on the validation set
val_predictions = car_model.predict(val_X)
# Calculating the mean absolute error on the validation set
val_mae = mean_absolute_error(val_y, val_predictions)
print("Validation Mean Absolute Error:", val_mae)  # Displaying the validation mean absolute error
# Making predictions on the validation set
print("First 5 predictions on validation set:", val_predictions[:5])  # Displaying the first 5 predictions
# Making predictions on the validation set 
print("First 5 actual values on validation set:", val_y[:5].values)  # Displaying the first 5 actual values
print('2nd setup complete')  # Indicating that the setup is complete
# Split the data into training and validation sets
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=0)
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    val_predictions = model.predict(val_X)
    return mean_absolute_error(val_y, val_predictions)
# Compare MAE with differing max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean_Absolute_Error: %d" %(max_leaf_nodes, my_mae))
# End of the code snippet