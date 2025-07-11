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
plt.figure(figsize=(16, 6))
# Line chart showing how FIFA ranking has changed over time
sns.lineplot(data=fifa_data)
