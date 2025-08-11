import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import display
from sklearn.feature_selection import mutual_info_regression

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
def plot_variance(pca, width=8, dpi=100):
    # Create figure
    fig, axs = plt.subplots(1, 2)
    n = pca.n_components_
    grid = np.arange(1, n + 1)
    # Explained variance
    evr = pca.explained_variance_ratio_
    axs[0].bar(grid, evr)
    axs[0].set(
        xlabel="Component", title="% Explained Variance", ylim=(0.0, 1.0)
    )
    # Cumulative Variance
    cv = np.cumsum(evr)
    axs[1].plot(np.r_[0, grid], np.r_[0, cv], "o-")
    axs[1].set(
        xlabel="Component", title="% Cumulative Variance", ylim=(0.0, 1.0)
    )
    # Set up figure
    fig.set(figwidth=8, dpi=100)
    return axs

def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores
df_filepath = r"E:\Courses\Python Kaggle\Datasets\Automobile\Automobile_data.csv"
df_filepath = df_filepath.replace("\\", "/")
df = pd.read_csv(df_filepath)
print(df.columns)
features = ["highway-mpg", "engine-size", "curb-weight", "horsepower",]

X = df.copy()
y = X.pop("price")
X = X.loc[:, features]

X = X.replace('?', np.nan).apply(pd.to_numeric, errors='coerce')
print("NaNs per column:\n", X.isna().sum())
X = X.fillna(X.median()) 

X_scaled = (X - X.mean()) / X.std(ddof=0) 

from sklearn.decomposition import PCA

# Create principal components
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Convert to dataframe
component_names = [f"PC{i+1}" for i in range(X_pca.shape[1])]
X_pca = pd.DataFrame(X_pca, columns=component_names)

print(X_pca.head())
loadings = pd.DataFrame(
    pca.components_.T,  # transpose the matrix of loadings
    columns=component_names,  # so the columns are the principal components
    index=X.columns,  # and the rows are the original features
)
loadings
# Look at explained variance
plot_variance(pca);
mi_scores = make_mi_scores(X_pca, y, discrete_features=False)
mi_scores
