# Focused on PCA feature engineering for Kaggle D25 Automobile dataset But its incomplete needs further revision.
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.feature_selection import mutual_info_regression

# --- load ---
df_filepath = r"E:\Courses\Python Kaggle\Datasets\Automobile\Automobile_data.csv"
df = pd.read_csv(df_filepath.replace("\\", "/"))

# --- clean y first and make a row mask ---
y_raw = df["price"].replace(['?', 'NA', 'N/A', 'None', '', 'nan'], np.nan)
y_num = pd.to_numeric(y_raw, errors='coerce')
mask = y_num.notna()

# keep only rows with numeric price
df = df.loc[mask].reset_index(drop=True)
y = y_num.loc[mask].reset_index(drop=True)

# --- features ---
features = ["highway-mpg", "engine-size", "curb-weight", "horsepower"]
X = df[features].replace(['?', 'NA', 'N/A', 'None', '', 'nan'], np.nan)
X = X.apply(pd.to_numeric, errors='coerce')

# impute + scale
X = pd.DataFrame(SimpleImputer(strategy='median').fit_transform(X), columns=features)
X_scaled = (X - X.mean()) / X.std(ddof=0)

# PCA
pca = PCA()
X_pca_arr = pca.fit_transform(X_scaled)
X_pca = pd.DataFrame(X_pca_arr, columns=[f"PC{i+1}" for i in range(X_pca_arr.shape[1])])

# Diagnostic helper
print(y.dtype, y.isna().sum())
print(X_pca.dtypes)
assert not X_pca.isna().any().any()


# MI helper
def make_mi_scores(X_df, y_series, discrete_features=False):
    mi = mutual_info_regression(X_df.to_numpy(), y_series.to_numpy(), discrete_features=discrete_features, random_state=0)
    return pd.Series(mi, name="MI Scores", index=X_df.columns).sort_values(ascending=False)

# run
mi_scores = make_mi_scores(X_pca, y, discrete_features=False)
print(mi_scores.head())

