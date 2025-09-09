# Preprocessing - Categorical Data

import pandas as pd
from sklearn import linear_model


# Categorical Data
cars = pd.read_csv("data.csv")
print(cars.to_string())

# One Hot Encoding
cars = pd.read_csv("data.csv")
ohe_cars = pd.get_dummies(cars[["Car"]])
print(ohe_cars.to_string())

# Predict CO2
cars = pd.read_csv("data.csv")
ohe_cars = pd.get_dummies(cars[["Car"]])
X = pd.concat([cars[["Volume", "Weight"]], ohe_cars], axis=1)
y = cars["CO2"]
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict(
    [[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
)
print(predictedCO2)

# Dummifying
colors = pd.DataFrame({"color": ["blue", "red", "green"]})
dummies = pd.get_dummies(colors, drop_first=True)
dummies["color"] = colors["color"]
print(dummies)
