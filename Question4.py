# Q4. How does the price of flights vary by airline? Create a boxplot to compare the prices of different
# airlines.

# Answer - 
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
df = pd.read_excel('flight_price.xlsx')
print(df.head())

# Assuming you have a DataFrame named flight_data with "Airline" and "Price" columns
# Create a boxplot to compare flight prices by airline
plt.figure(figsize=(12, 6))
sns.boxplot(x='Airline', y='Price', data=df)
plt.xticks(rotation=90)  # Rotate x-axis labels for readability
plt.xlabel('Airline')
plt.ylabel('Price')
plt.title('Flight Prices by Airline (Boxplot)')
plt.show()