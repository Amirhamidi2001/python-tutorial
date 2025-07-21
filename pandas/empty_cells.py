# Pandas - Cleaning Empty Cells

import pandas as pd


# Remove Rows
df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df.to_string())

# Remove all rows with NULL values
df = pd.read_csv("data.csv")
df.dropna(inplace=True)
print(df.to_string())

# Replace Empty Values
df = pd.read_csv("data.csv")
df.fillna(130, inplace=True)

# Replace Only For Specified Columns
df = pd.read_csv("data.csv")
df.fillna({"Calories": 130}, inplace=True)

# Replace Using Mean, Median, or Mode
df = pd.read_csv("data.csv")
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

# Calculate the MEDIAN
df = pd.read_csv("data.csv")
x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)

# Calculate the MODE
df = pd.read_csv("data.csv")
x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace=True)
