### Session 5 Data types and missing values
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

### Session 6 Renaming and combining
reviews.rename(columns={'points' : 'score'}, inplace=True)
# check if the column was renamed
print(reviews.columns)  # This will show the current column names, including 'score' if the rename was successful.

reviews.rename(index={0: 'first_entry', 1: 'second_entry'}, inplace=True)
print(reviews.head(2))  # This will show the first two rows with the new index names.

reviews = reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns') # This renames the index and columns axes.
print(reviews.head(2))  # This will show the first two rows with the new axis names.


### Combining DataFrames
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 5)
Canadian_videos = pd.read_csv(r"E:\Courses\Python Kaggle\Datasets\archive\CAvideos.csv", index_col=0)
Great_britain_videos = pd.read_csv(r"E:\Courses\Python Kaggle\Datasets\archive\GBvideos.csv", index_col=0)

# concat() method
combined_videos = pd.concat([Canadian_videos, Great_britain_videos]) # Concatenates the two DataFrames vertically (row-wise)
print(combined_videos.shape)  # Check the number of rows and columns
print(combined_videos.head()) # Preview the first few rows
print(combined_videos.tail()) # Preview the last few rows

### join() method
left = Canadian_videos.set_index(['title', 'trending_date'])
right = Great_britain_videos.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')
print(left.join(right, lsuffix='_CAN', rsuffix='_UK').head())  # Preview the first few rows of the joined DataFrame


#  EX 1
"""
region_1 and region_2 are pretty uninformative names for locale columns in the dataset.
Create a copy of reviews with these columns renamed to region and locale, respectively.
"""
renamed = reviews.rename(columns={'region_1' : 'region', 'region_2' : 'locale'})
print(renamed.head())  # Preview the first few rows of the renamed DataFrame

# EX 2
"""
Set the index name in the dataset to wines.
"""
reindexed = reviews.rename_axis("wines", axis='rows')
print(reindexed.head())  # Preview the first few rows of the reindexed DataFrame

#  EX 3
"""
The Things on Reddit dataset includes product links from a selection of 
top-ranked forums ("subreddits") on reddit.com. Run the cell below to load a 
dataframe of products mentioned on the /r/gaming subreddit and another dataframe
for products mentioned on the r//movies subreddit.
"""
# combined_products = pd.concat([gaming_products, movie_products])

