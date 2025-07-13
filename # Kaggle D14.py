# Session 1 
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

# Session 2
import matplotlib.pyplot as plt
import seaborn as sns

print ("Setup Complete")
insurance_filepath = r"E:\Courses\Python Kaggle\Datasets\insurance.csv"
insurance_filepath = insurance_filepath.replace("\\", "/")  # Ensure the path is correctly formatted
# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)
print(insurance_data.head(10))  # Display the first 10 rows of the DataFrame
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
plt.title("BMI vs Charges")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()  # Show the plot
# Regression plot showing the relationship between BMI and Charges
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title("BMI vs Charges with Regression Line")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()  # Show the plot
# Color coded scatter plot.
# Scatter plot showing the relationship between BMI and Charges with hue based on smoker status
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
plt.title("BMI vs Charges")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()
sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)
plt.title("BMI vs Charges with Regression Line and Smoker Status")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()  # Show the plot

## Categorical scatter plots
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
plt.title("Charges by Smoker Status")
plt.xlabel("Smoker Status")
plt.ylabel("Charges")
plt.show()  # Show the plot