import pandas as pd

melbourne_filepath = r"E:\Courses\Python Kaggle\Datasets\melb_data.csv"
melbourne_filepath = melbourne_filepath.replace("\\","/")
melb_data = pd.read_csv(melbourne_filepath)
print(melb_data.describe())
print(melb_data.columns)
melb_data= melb_data.dropna(axis=0)
print(melb_data.describe())
y = melb_data.Price # we are aiming to predict the price so this is our prediction target
melb_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude'] # selecting features that will help predict the price
X = melb_data[melb_features]
print(X.describe())
print(X.head())

from sklearn.tree import DecisionTreeRegressor

melb_model = DecisionTreeRegressor(random_state=1) # Step 1 : Defining Model type & Specifying a number for random_state to ensure same results each run
melb_model.fit(X,y) # Fitting Model
print('Making preparation for the following 5 houses:')
print(X.head())
print('The predictions are')
print(melb_model.predict(X.head()))
