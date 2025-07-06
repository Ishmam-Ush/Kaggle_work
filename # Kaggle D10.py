# Label based selection
import pandas as pd
Wine_review = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)
print(Wine_review)
print(Wine_review.loc[0,'country'])
print(Wine_review.loc[:,['winery','variety','points']])
print(Wine_review.set_index("title"))
print(Wine_review.country == "Italy")
print(Wine_review.loc[Wine_review.country == "Italy"])
