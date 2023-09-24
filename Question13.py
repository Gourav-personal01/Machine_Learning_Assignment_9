# Q13. How does the type of app affect its price? Create a bar chart to compare average prices by app type.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming you already have it loaded)
df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')

# Group the data by 'Type' and calculate the average price for each type
average_prices_by_type = df.groupby('Type')['Price'].mean()

# Create a bar chart to visualize the average prices by app type
plt.figure(figsize=(10, 6))
average_prices_by_type.plot(kind='bar', color='skyblue')
plt.xlabel('App Type')
plt.ylabel('Average Price')
plt.title('Average Prices by App Type')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.show()
