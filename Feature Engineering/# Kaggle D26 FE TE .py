# Target Encoding Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 


autos_filepath = r"E:\Courses\Python Kaggle\Datasets\Automobile\Automobile_data.csv"
autos = pd.read_csv(autos_filepath.replace('\\', '/'))

autos["price"] = pd.to_numeric(autos["price"].replace('[\$,]', '', regex=True), errors='coerce')
autos["make_encoded"] = autos.groupby("make")["price"].transform("mean")
print(autos[["make", "price", "make_encoded"]].head(10))

sns.set_style("whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)
warnings.filterwarnings('ignore')

movie_filepath = r"E:\Courses\Python Kaggle\Datasets\movielens1m.csv\movielens1m.csv"
movie_data = pd.read_csv(movie_filepath.replace("\\", "/"))
movie_data = movie_data.astype(np.uint8, errors='ignore') # reduce memory footprint
print(f"Number of Unique Zipcodes: {movie_data['Zipcode'].nunique()}")

X = movie_data.copy()
y = X.pop('Rating')

# creating a 25% split to train the target encoder

X_encode = X.sample(frac=0.25)
y_encode = y[X_encode.index]
X_pretrain = X.drop(X_encode.index)
y_train = y[X_pretrain.index]

from category_encoders import MEstimateEncoder

# Create the encoder instance. Choose m to control noise.
encoder = MEstimateEncoder(cols=["Zipcode"], m=5.0)

# Fit the encoder on the encoding split.
encoder.fit(X_encode, y_encode)

# Encode the Zipcode column to create the final training data
X_train = encoder.transform(X_pretrain)

plt.figure(dpi=90)
ax = sns.distplot(y, kde=False, norm_hist=True)
ax = sns.kdeplot(X_train.Zipcode, color='r', ax=ax)
ax.set_xlabel("Rating")
ax.legend(labels=['Zipcode', 'Rating']);
plt.show()