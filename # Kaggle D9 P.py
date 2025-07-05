# Indexing Selecting and Assigning

import pandas as pd
Wine_review = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(Wine_review)
print(pd.set_option("display.max_rows", 5))

# calling individual column or definite content of a column

print(Wine_review.country)
print(Wine_review['country'])
print(Wine_review['country'][1])

# calling rows
print(Wine_review.loc[:])
print(Wine_review.iloc[1])


print(pd.Series([31,32,33], index=['sales 2017', 'sales 2018', 'sales 2019'], name='Sales'))

print(Wine_review.head())
print(Wine_review.tail())
print(Wine_review.shape)
print(Wine_review.columns)
print(Wine_review.index)
print(Wine_review.dtypes)
