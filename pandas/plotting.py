# Pandas - Plotting

import pandas as pd
import matplotlib.pyplot as plt


# Plotting
df = pd.read_csv("data.csv")
df.plot()
plt.show()

# Scatter Plot
df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()


df.plot(kind="scatter", x="Duration", y="Maxpulse")
plt.show()

# Histogram
df["Duration"].plot(kind="hist")
plt.show()
