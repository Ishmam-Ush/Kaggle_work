import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())

# Summary functions
# To get a summary of the DataFrame, you can use the describe() method.
# This will return a summary of the numerical columns in the DataFrame.
print(reviews.points.describe())
# To get the mean of a specific column, you can use the mean() method.
# This will return the average value of the points column.
print(reviews.points.mean())
# To see a set of unique values in a column, use the unique() method.
# This will return an array of unique values in the taster_name column.
print(reviews.taster_name.unique())
# To see a list of unique values in a column and how many times each value appears, use the value_counts() method.
# This will return a Series with the unique values as the index and the counts as the values.
print(reviews.taster_name.value_counts()) 