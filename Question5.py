# Q5. Are there any outliers in the dataset? Identify any potential outliers using a boxplot and describe how
# they may impact your analysis.

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
df = pd.read_excel('flight_price.xlsx')
print(df.head())

plt.figure(figsize=(8, 6))
sns.boxplot(x='Price', data=df)
plt.xlabel('Price')
plt.title('Boxplot of Flight Prices')
plt.show()

# Lower Outliers: These are data points below the lower whisker

# Upper Outliers: These are data points above the upper whisker.

# Modeling: In some cases, outliers can significantly affect the performance of statistical or machine learning models. They may cause models to be less robust or lead to incorrect predictions.