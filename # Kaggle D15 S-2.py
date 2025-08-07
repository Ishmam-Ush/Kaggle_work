# Choosing Plot types and Custom Styles
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

spotify_filepath = r"E:\Courses\Python Kaggle\Datasets\spotify.csv"
spotify_filepath = spotify_filepath.replace("\\","/")
spotify_data = pd.read_csv(spotify_filepath, index_col='Date', parse_dates=True)
plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.show()
sns.set_style("dark")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.show()

# EXERCISE 

# darkgrid
sns.set_style("darkgrid")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.title("DARKGRID")
plt.show()
# whitegrid
sns.set_style("whitegrid")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.title("WHITEGRID")
plt.show()
# White
sns.set_style("white")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.title("WHITE")
plt.show()
# TICKS
sns.set_style("ticks")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.title("TICKS")
plt.show()
