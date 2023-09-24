# Q11. Are there any missing values in the dataset? Identify any missing values and describe how they may
# impact your analysis.

# Answer - We can hanlde the missing value by delete a particular row or column or either replace it with the average of that column.

import pandas as pd
import seaborn as sns

# Load the dataset from the URL
df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')

# Display the first few rows of the dataset
print(df.head())

# Get information about the dataset, including data types and non-null counts
print(df.info())

# Check for missing values and display the count of missing values for each column
print(df.isnull().sum())

# Handle missing values in the 'Type' column by removing rows with missing values in that column
handle_missing_values = df.dropna(subset=['Type'])

# Display the DataFrame after handling missing values
print(handle_missing_values)
