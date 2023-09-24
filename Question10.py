# Q10. How does the rating of apps vary by category? Create a boxplot to compare the ratings of different
# app categories.


import pandas as pd
import seaborn as sns
df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')
print(df.head())

sns.boxplot(x='App',y='Rating',data=df)