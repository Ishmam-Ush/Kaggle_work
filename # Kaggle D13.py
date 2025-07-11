# Session 1 
# Data visualization 
# seaborn
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
fifa_filepath = r"E:/Courses/Python Kaggle/Datasets/FIFA/fifa_ranking_202406.csv"
# Read the file into a variable fifa
fifa_data = pd.read_csv(fifa_filepath, index_col="rank_date", parse_dates=True)
print(fifa_data.head(198))  # Display the first selected rows of the DataFrame

# Set the width and height of the figure
plt.figure(figsize=(12, 6))
# Line chart showing how FIFA ranking has changed over time
sns.lineplot(data=fifa_data)
plt.title("FIFA Ranking Over Time")
plt.xlabel("Date")
plt.ylabel("Ranking")

plt.show()  # Show the plot

# Session 2 
# Line charts

spotify_filepath = r"E:\Courses\Python Kaggle\Datasets\spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
print(spotify_data.head(10))  # Display the first 10 rows of the DataFrame
print(spotify_data.tail(10))  # Display the last 10 rows of the DataFrame
plt.title("Spotify Daily Streams")
plt.xlabel("Date")
plt.ylabel("Streams")
sns.lineplot(data=spotify_data)
plt.show()  # Show the plot

