# NumPy Summations

import numpy as np


# Addition
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4])
newarr = np.add(arr1, arr2)
print(newarr)

# Summations
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4])
newarr = np.sum([arr1, arr2])
print(newarr) 

# Summation Over an Axis
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

# Cummulative Sum
arr = np.array([1, 2, 3, 4])
newarr = np.cumsum(arr)
print(newarr) 
