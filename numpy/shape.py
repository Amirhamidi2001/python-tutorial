# NumPy Array Shape

import numpy as np


# Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# Get the Shape of an Array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("shape of array :", arr.shape)
