# Bar charts and heatmaps
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

flight_filepath = r"E:/Courses/Python Kaggle/Datasets/flight_delays.csv"
flight_filepath = flight_filepath.replace("\\", "/")  # Ensure the path is correctly formatted
# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month", parse_dates=True)
print(flight_data)  # Display the first 10 rows of the DataFrame

## Bar chart showing the average delay per month of Spirit Airlines
# Set the width and height of the figure 
plt.figure(figsize=(10,6))
# Add title 
plt.title("Average delay per month of the Spirit Airlines")
# Bar chart showing the average delay per month of Spirit Airlines
sns.barplot(x=flight_data.index, y=flight_data['NK'], palette="viridis")
# Add label for the vertical axis
plt.ylabel("Arrival Delay (in minutes)")
# Show the plot
plt.show()

# Heatmap showing the average delay per month for each Airlines
plt.figure(figsize=(10,6))
# Add title
plt.title("Average delay per month for each Airlines")
# Heatmap showing the average delay per month for each Airlines
sns.heatmap(data=flight_data, annot=True)

# Add label for the horizontal axis
plt.xlabel("Airlines")

plt.show()  # Show the plot

### Exercise
# EX-1
# Path of the file to read
ign_filepath = r"E:\Courses\Python Kaggle\Datasets\ign_scores.csv"
ign_filepath = ign_filepath.replace("\\", "/")  # Ensure the path is correctly formatted
# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath,index_col="Platform", parse_dates=True)
print(ign_data.head(22))  # Display the first 10 rows of the DataFrame
