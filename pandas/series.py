# Pandas Series

import pandas as pd


# What is a Series?
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Labels
print(myvar[0])

# Create Labels
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

# Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Create a Series using only data
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

# DataFrames
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
myvar = pd.DataFrame(data)
print(myvar)
