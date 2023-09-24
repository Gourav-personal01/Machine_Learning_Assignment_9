# Q14. What are the top 10 most popular apps in the dataset? Create a frequency table to identify the apps
# with the highest number of installs.

import pandas as pd

# Load the dataset (assuming you already have it loaded)
# Replace 'your_dataset.csv' with the actual dataset file name or URL
df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')

# Create a frequency table of app names and their corresponding install counts
app_install_counts = df[['App', 'Installs']].groupby('App').sum()

# Sort the frequency table by install counts in descending order
app_install_counts_sorted = app_install_counts.sort_values(by='Installs', ascending=False)

# Select the top 10 most popular apps
top_10_apps = app_install_counts_sorted.head(10)

# Display the top 10 most popular apps
print(top_10_apps)
