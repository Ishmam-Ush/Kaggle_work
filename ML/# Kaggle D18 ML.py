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
X = melb_data[melb_features] # Selecting features from the dataset
print(X.describe())  # Describing the features
print(X.head())  # Displaying the first few rows of the features

from sklearn.tree import DecisionTreeRegressor
melb_model = DecisionTreeRegressor(random_state=1)  # Step 1: Defining the model type and setting random_state for reproducibility
melb_model.fit(X, y)  # Fitting the model to the data
from sklearn.metrics import mean_absolute_error
predicted_home_prices = melb_model.predict(X)  # Making predictions
mean_absolute_error(y, predicted_home_prices)  # Calculating the mean absolute error of the predictions
print("Mean Absolute Error:", mean_absolute_error(y, predicted_home_prices))  # Displaying the mean absolute error
print(melb_model.predict(X.head()))  # Predicting the price for the first 5 houses
print("Setup Complete")

from sklearn.model_selection import train_test_split
# Splitting the dataset into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=1)

# Defining the model again for the training set
melb_model = DecisionTreeRegressor(random_state=1)
# Fitting the model to the training data
melb_model.fit(train_X, train_y)
# Making predictions on the validation set
val_predictions = melb_model.predict(val_X)
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
    