## session 4 grouping and sorting
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())

print(reviews.groupby('points').points.count())
print(reviews.groupby('points').price.min())
# selecting the name of the first wine reviewed from each winery in the dataset
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

# Grouping by multiple columns
print(reviews.groupby(['country', 'province']).apply(lambda df:df.loc[df.points.idxmax()]))
# use of agg to apply multiple functions to a grouped DataFrame
print(reviews.groupby(['country']).price.agg([len,min,max]))

# multiple aggregations on multiple columns
countries_reviewed = reviews.groupby(['country','province']).description.agg([len])
print(countries_reviewed)
print(countries_reviewed.reset_index())

### Sorting
# sort values ascending sort by default
print(countries_reviewed.sort_values(by='len'))
# sort values descending
print(countries_reviewed.sort_values(by='len', ascending=False))
print(countries_reviewed.sort_index())
# sorting more than one column at a time
print(countries_reviewed.sort_values(by=['country', 'len']))

# EX 1
"""
Who are the most common wine reviewers in the dataset? Create a Series whose index is 
the taster_twitter_handle category from the dataset, and whose values count how many reviews each person wrote.    
"""
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print("Reviews written by each taster:\n", reviews_written)

# EX 2
"""
What is the best wine I can buy for a given amount of money? Create a Series whose index is wine
prices and whose values is the maximum number of points a wine costing that much was given in a review. 
Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).    
"""
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print("Best rating per price:\n", best_rating_per_price)

# EX 3
"""
What are the minimum and maximum prices for each variety of wine? 
Create a DataFrame whose index is the variety category from the dataset and
whose values are the min and max values thereof.
"""
price_extremes = reviews.groupby('variety').price.agg(['min','max'])
print("Price extremes per variety:\n", price_extremes)

# EX 4
"""
What are the most expensive wine varieties? Create a variable 
sorted_varieties containing a copy of the dataframe from the 
previous question where varieties are sorted in descending order
based on minimum price, then on maximum price (to break ties).    
"""
sorted_varieties = price_extremes.sort_values(by=['min','max'], ascending=False)
print("Sorted varieties by price:\n", sorted_varieties)

# EX 5
"""
Create a Series whose index is reviewers and whose values is the average 
review score given out by that reviewer. Hint: you will need the taster_name and points columns.
"""
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
print("Average review score by reviewer:\n", reviewer_mean_ratings)

# EX 6
"""
What combination of countries and varieties are most common? 
Create a Series whose index is a MultiIndexof {country, variety} pairs.
For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}.
Sort the values in the Series in descending order based on wine count.
"""
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)
print("Most common country-variety combinations:\n", country_variety_counts)
