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

# EXERCISE 1
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame([{"Apples":30,"Bananas":21}])
print(fruits)
# EX 2
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame([{"Apples":35,"Bananas":21},{"Apples":41,"Bananas":34}],
index = ["2017 Sales","2018 Sales"]
)
print(fruit_sales)
# EX 3
items = ['Flour', 'Milk', 'Eggs', 'Spam']
portion = ["4 cups", "1 cup", "2 large", "1 can"]

recipe = pd.Series(portion, index=items, name="Dinner")
print(recipe)
# EX 4
reviews = pd.read_csv("E:\Courses\Python Kaggle\Datasets\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=1)
print(reviews)

# EX 5
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv")
print(animals)

# native accessors- Columns in a pandas DataFrame can be accessed by calling like this: 
print(Wine_review.country)
print(Wine_review['description'])
print(Wine_review['points'])
print(Wine_review['country'][5])
print(Wine_review['country'][5:10])
print(Wine_review.iloc[5])
print(Wine_review.iloc[:,0])
print(Wine_review.iloc[:3,0])
print(Wine_review.iloc[:5,3])
print(Wine_review.iloc[1:5,0])
print(Wine_review.iloc[[0,1,2],0])
print(Wine_review.iloc[-5:])
