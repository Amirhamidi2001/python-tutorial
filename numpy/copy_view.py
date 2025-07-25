# NumPy Array Copy vs View

import numpy as np


# The Difference Between Copy and View

# Make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# Make a view, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Make Changes in the VIEW
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# Check if Array Owns its Data
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
