# Random Permutations

from numpy import random
import numpy as np


# Shuffling Arrays
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# Generating Permutation of Arrays
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
