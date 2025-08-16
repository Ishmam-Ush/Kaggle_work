# Data Leakage
import pandas as pd 
# lead data
data = pd.read_csv(r"E:\Courses\Python Kaggle\Datasets\Credir card data\AER_credit_card_data.csv")

# set target
y = data.card 
# set predictors
X = data.drop(['card'], axis=1)

print("Number of rows in the dataset:", X.shape[0])
print(X.head())

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Since there is no preprocessing, we don't need a pipeline (used anyway as best practice!)
my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y, 
                            cv=5,
                            scoring='accuracy')

print("Cross-validation accuracy: %f" % cv_scores.mean())
expenditures_cardholders = X.expenditure[y]
expenditures_noncardholders = X.expenditure[~y]

print('Fraction of those who did not receive a card and had no expenditures: %.2f' \
    %((expenditures_noncardholders == 0).mean()))
print('Fraction of those who received a card and had no expenditures: %.2f' \
    %(( expenditures_cardholders == 0).mean()))

