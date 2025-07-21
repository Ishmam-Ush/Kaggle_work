import pandas as pd

melbourne_filepath = r"E:\Courses\Python Kaggle\Datasets\melb_data.csv"
melbourne_filepath = melbourne_filepath.replace("\\","/")
melb_data = pd.read_csv(melbourne_filepath)
print(melb_data.describe())
print(melb_data.columns)
melb_data= melb_data.dropna(axis=0)
print(melb_data.describe())