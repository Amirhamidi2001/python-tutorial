# Pandas DataFrames

import pandas as pd


# What is a DataFrame?
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df)

# refer to the row index:
print(df.loc[0])

# use a list of indexes:
print(df.loc[[0, 1]])

# Named Indexes
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)

# Locate Named Indexes
print(df.loc["day2"])
