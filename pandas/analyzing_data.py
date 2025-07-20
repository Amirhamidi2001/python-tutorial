# Pandas - Analyzing DataFrames

import pandas as pd


# Viewing the Data
df = pd.read_csv("data.csv")
print(df.head(10))

# return the top 5 rows
print(df.head())

# viewing the last rows of the DataFrame
print(df.tail())

# Info About the Data
print(df.info())
