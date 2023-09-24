# Q3. What is the range of prices in the dataset? What is the minimum and maximum price?

import pandas as pd
import seaborn as sns
df = pd.read_excel('flight_price.xlsx')
print(df.head())

# Minimum Price Value
print(df[['Price']].min())

# Maximum Price Value
print(df[['Price']].max())