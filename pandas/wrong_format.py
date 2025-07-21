# Pandas - Cleaning Data of Wrong Format

import pandas as pd


# Convert Into a Correct Format
df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
print(df.to_string())

# Removing Rows
df.dropna(subset=["Date"], inplace=True)
