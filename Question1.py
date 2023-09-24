# Q1. Load the flight price dataset and examine its dimensions. How many rows and columns does the
# dataset have?
import pandas as pd

df = pd.read_excel('flight_price.xlsx')
print(df.head())

print(df.shape)

print(f"rows are : {df.shape[0]}")
print(f"columns are : {df.shape[1]}")