# Q9. Load the Google Playstore dataset and examine its dimensions. How many rows and columns does
# the dataset have?

import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')
print(df.head())

print(f"rows are : {df.shape[0]}")
print(f"columns are : {df.shape[1]}")