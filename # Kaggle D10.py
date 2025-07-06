# Label based selection
# sourcery skip: remove-redundant-slice-index
import pandas as pd
Wine_review = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(Wine_review)
print(Wine_review.loc[0,'country'])
print(Wine_review.loc[:,['winery','variety','points']])
print(Wine_review.set_index("title"))
print(Wine_review.country == "Italy")
print(Wine_review.loc[Wine_review.country == "Italy"])
print(Wine_review.loc[(Wine_review.country == "Italy") & (Wine_review.points >= 90)])
print(Wine_review.loc[(Wine_review.country == "Italy") | (Wine_review.points >= 90)])
print(Wine_review.loc[Wine_review.country.isin(["Italy", "France"])])
print(Wine_review.loc[Wine_review.price.notnull()])


# Assigning constant value to a column
# This will add a new column 'critic' with the value 'everyone' for all rows
Wine_review['critic']= 'everyone'
print(Wine_review['critic'])

# Assigning an iterable to a column
# This will add a new column 'critic' with the values from the list
Wine_review['index backwards'] = range(len(Wine_review), 0 ,-1)
print(Wine_review['index backwards'])


# Ex 1
# Select the description column from reviews and assign the result to the variable desc.
desc = Wine_review['description']
print(desc)

# Ex 2
# Select the first value from the description column of reviews, assigning it to variable first_description.
first_description = Wine_review.description[0]
print(first_description)

# Ex 3
# Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
first_row = Wine_review.iloc[0]
print(first_row)

# Ex 4
# Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
first_descriptions = Wine_review.description.iloc[0:10]

# Ex 5
# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
sample_reviews = Wine_review.loc[[1, 2, 3, 5, 8]]
print(sample_reviews)

# Ex 6
# Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100.
df = Wine_review.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
print(df)
# Ex 7
# Create a variable df containing the country and variety columns of the first 100 records.
df = Wine_review.loc[:99, ['country', 'variety']]
print(df)
# Ex 8
# Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = Wine_review.loc[Wine_review.country == "Italy"]
print(italian_wines)
# Ex 9
# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
top_oceania_wines = Wine_review.loc[(Wine_review.country.isin(["Australia", "New Zealand"])) & (Wine_review.points >= 95)]
print(top_oceania_wines)