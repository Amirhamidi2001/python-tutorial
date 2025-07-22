# Pandas - Removing Duplicates

import pandas as pd

# Discovering Duplicates
df = pd.read_csv("data.csv")
print(df.duplicated())

# Removing Duplicates
df.drop_duplicates(inplace=True)
print(df.to_string())
