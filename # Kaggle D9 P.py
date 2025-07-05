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
print(Wine_review.loc[])
print(Wine_review.iloc[1])



