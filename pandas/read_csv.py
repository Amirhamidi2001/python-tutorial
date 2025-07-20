# Pandas Read CSV

import pandas as pd


# Read CSV Files
df = pd.read_csv("data.csv")
print(df.to_string())

# to_string
print(df)

# max_rows
print(pd.options.display.max_rows)

# change the maximum rows
pd.options.display.max_rows = 9999
df = pd.read_csv("data.csv")
print(df)
