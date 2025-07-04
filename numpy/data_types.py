# NumPy Data Types

import numpy as np


# Checking the Data Type of an Array

# Get the data type of an array object
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Get the data type of an array containing strings
arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)

# Creating Arrays With a Defined Data Type

# Create an array with data type string
arr = np.array([1, 2, 3, 4], dtype="S")
print(arr)
print(arr.dtype)

# Create an array with data type 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype="i4")
print(arr)
print(arr.dtype)

# What if a Value Can Not Be Converted

"""
arr = np.array(['a', '2', '3'], dtype='i') 
"""

# Converting Data Type on Existing Arrays

# Change data type from float to integer by using 'i' as parameter value
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype("i")
print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
