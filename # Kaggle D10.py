# Label based selection
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