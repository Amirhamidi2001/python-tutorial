# SciPy Matlab Arrays

from scipy import io
import numpy as np


# Exporting Data in Matlab Format
arr = np.arange(10)
io.savemat("arr.mat", {"vec": arr})

# Import Data from Matlab Format
arr = np.array(
    [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]
)

# Export:
io.savemat("arr.mat", {"vec": arr})

# Import:
mydata = io.loadmat("arr.mat")
print(mydata)
print(mydata["vec"])

# squeeze_me=True
mydata = io.loadmat("arr.mat", squeeze_me=True)
print(mydata["vec"])
