##session 3 summary function and maps
import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())

### Summary functions
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

### MAPS
"""
A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values.
In data science we often have a need for creating new representations from existing data, or for transforming data from the format 
it is in now to the format that we want it to be in later. Maps are what handle this work, making them extremely important for 
getting your work done!
"""
# To apply a function to each element in a Series, we can use the map() method.
# This will apply the function to each element in the Series and return a new Series with the
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
print(reviews.points.map(lambda p: p - review_points_mean).head())

# Apply method 
#def remean_points(row):
#    row.points = row.points - review_points_mean
#    return row
#reviews.apply(remean_points, axis ='columns')
#print(reviews.apply(remean_points, axis ='columns').head())

# Note that map() and apply() return new, transformed Series and DataFrames
# Combining columns in a DataFrame
# To combine two columns in a DataFrame, you can use the + operator.
# This will concatenate the two columns and return a new Series.
print(reviews.country + " - " + reviews.region_1)
"""
These operators are faster than map() or apply() because they use speed ups built into pandas.
All of the standard Python operators (>, <, ==, and so on) work in this manner.However, they 
are not as flexible as map() or apply(), which can do more advanced things,like applying 
conditional logic, which cannot be done with addition and subtraction alone.
"""

# EX 1
# What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()
print("Median points:", median_points)

# EX 2
# What countries are represented in the dataset? (Your answer should not include any duplicates.)
# can be solved using the unique() method
countries = reviews.country.unique()
print("Countries represented in the dataset:", countries)

# EX 3
# How often does each country appear in the dataset?
# Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
reviews_per_country = reviews.country.value_counts()
print("Reviews per country:\n", reviews_per_country)

# EX 4 
# Create variable centered_price containing a version of the price column with the mean price subtracted.
# (Note: this 'centering' transformation is a common preprocessing step before applying various machine learning algorithms.)
centered_price = reviews.price - reviews.price.mean()
print("Centered price:\n", centered_price.head())

# EX 5
# I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine
# with the title of the wine with the highest points-to-price ratio in the dataset.
bargin_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargin_idx , 'title']
print("Best bargain wine:", bargain_wine)

# EX 6
"""
There are only so many words you can use when describing a bottle of wine. 
Is a wine more likely to be "tropical" or "fruity"? Create a Series descriptor_counts 
counting how many times each of these two words appears in the description column in the dataset. 
(For simplicity, let's ignore the capitalized versions of these words.)
"""
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop,n_fruity], index= ["tropical"," fruity"])
print("Descriptor counts:\n", descriptor_counts)

# EX 7
"""
We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand 
- we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but 
less than 95 is 2 stars. Any other score is 1 star. Also, the Canadian Vintners Association bought a lot of ads on the site,
so any wines from Canada should automatically get 3 stars, regardless of points.Create a series star_ratings with the number 
of stars corresponding to each review in the dataset.
"""
def stars(row):
    if row.country == 'Canada' or row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')
print("Star ratings:\n", star_ratings.head())

## session 4 grouping and sorting
import pandas as pd
pd.set_option('display.max_rows', 5)

print(reviews.groupby('points').points.count())
print(reviews.groupby('points').price.min())
# selecting the name of the first wine reviewed from each winery in the dataset
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

# Grouping by multiple columns
print(reviews.groupby(['country', 'province']).apply(lambda df:df.loc[df.points.idxmax()]))

