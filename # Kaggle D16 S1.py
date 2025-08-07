# Final Project
# Exercise 
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Load data
my_filepath = r"E:\Courses\Python Kaggle\Datasets\salaries.csv"
my_filepath = my_filepath.replace("\\","/")
my_data = pd.read_csv(my_filepath)
print(my_data.head(15))