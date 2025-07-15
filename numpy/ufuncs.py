# NumPy ufuncs

import numpy as np


# What is Vectorization
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)

# use ufuncs
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


# Create Your Own ufunc
def myadd(x, y):
    return x + y


myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a Function is a ufunc
print(type(np.add))

print(type(np.concatenate))

"""
print(type(np.blahblah)) 
"""

# Use an if statement to check if the function is a ufunc or not
if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")
