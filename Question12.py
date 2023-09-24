# Q12. What is the relationship between the size of an app and its rating? Create a scatter plot to visualize
# the relationship.

# Answer - 

import pandas as pd
import seaborn as sns

# Load the dataset from the URL
df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')

# Display the first few rows of the dataset
print(df.head())

sns.scatterplot(x='App',y='Rating',data=df)