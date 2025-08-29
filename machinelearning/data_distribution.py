# Data Distribution

import numpy as np
import matplotlib.pyplot as plt


# How Can we Get Big Data Sets?
x = np.random.uniform(0.0, 5.0, 250)
print(x)

# Histogram
x = np.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()

# Big Data Distributions
x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

# Normal Data Distribution
x = np.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()
