# Rounding Decimals

import numpy as np


# Truncation
arr = np.trunc([-3.1666, 3.6667])
print(arr)

arr = np.fix([-3.1666, 3.6667])
print(arr)

# Rounding
arr = np.around(3.1666, 2)
print(arr)

# Floor
arr = np.floor([-3.1666, 3.6667])
print(arr)

# Ceil
arr = np.ceil([-3.1666, 3.6667])
print(arr)
