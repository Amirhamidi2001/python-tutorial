# Machine Learning - Multiple Regression

import pandas as pd
from sklearn.linear_model import LinearRegression


# Load dataset
df = pd.read_csv("data.csv")

# Define independent (X) and dependent (y) variables
X = df[["Weight", "Volume"]]
y = df["CO2"]

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Prediction example 1
predicted_co2_1 = model.predict([[2300, 1300]])
print(predicted_co2_1[0])

# Model coefficients
print(model.coef_)
print(model.intercept_)

# Prediction example 2
predicted_co2_2 = model.predict([[3300, 1300]])
print(predicted_co2_2[0])
