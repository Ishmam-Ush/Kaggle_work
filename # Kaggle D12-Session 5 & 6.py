# dtype 
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())

print(reviews.dtypes) # check data types of each column
print(reviews.price.dtype) # check price data type
print(reviews.points.astype('float64')) # convert points to float64
print(reviews.index.dtype) # convert index to datetime
print(reviews[pd.isnull(reviews.country)]) # check for NaN values in the country column
print(reviews.country.fillna("unknown")) # fillna replaces NaN values with the specified value

print(reviews.taster_twitter_handle.replace("@kerinokeefe","@kerino")) # replace a value in the taster_twitter_handle column 
# we can use replace to change any value in a column to another value or in cse of changing a NaN value

# EX 1
"""
What is the data type of the points column in the dataset?
"""
dtype = reviews.points.dtype

# EX 2
"""
Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.
"""
point_strings = reviews.points.astype('str')
print(point_strings)

# EX 3
"""
Sometimes the price column is null. How many reviews in the dataset are missing a price?
"""
n_missing_prices = pd.isnull(reviews.price).sum()
print("Number of reviews missing a price:", n_missing_prices)

# EX 4
"""
What are the most common wine-producing regions? 
Create a Series counting the number of times each value occurs
in the region_1 field. This field is often missing data, so replace missing
values with Unknown. Sort in descending order.
"""
reviews_per_region = reviews.region_1.fillna("unknown").value_counts().sort_values(ascending=False)
print("Reviews per region:\n", reviews_per_region)