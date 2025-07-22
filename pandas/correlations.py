# Pandas - Data Correlations

import pandas as pd


# Finding Relationships
df = pd.read_csv("data.csv")
print(df.corr())
