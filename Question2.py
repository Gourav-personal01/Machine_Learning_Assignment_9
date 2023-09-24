# Q2. What is the distribution of flight prices in the dataset? Create a histogram to visualize the
# distribution.
import pandas as pd
import seaborn as sns
df = pd.read_excel('flight_price.xlsx')
print(df.head())
print(df[['Price']])

sns.histplot(df[['Price']])
