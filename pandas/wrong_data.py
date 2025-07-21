# Pandas - Fixing Wrong Data

import pandas as pd


# Replacing Values
df = pd.read_csv("data.csv")
df.loc[7, "Duration"] = 45
print(df.to_string())

# Loop through all values in the "Duration" column
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Removing Rows
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
