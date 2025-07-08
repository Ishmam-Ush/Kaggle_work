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