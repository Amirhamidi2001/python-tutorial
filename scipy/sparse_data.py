# SciPy Sparse Data

import numpy as np
from scipy.sparse import csr_matrix


# CSR Matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

# Sparse Matrix Methods
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

# Counting nonzeros with the count_nonzero() method
print(csr_matrix(arr).count_nonzero())

# Removing zero-entries from the matrix with the eliminate_zeros() method
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

# Eliminating duplicate entries with the sum_duplicates() method
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

# Converting from csr to csc with the tocsc() method
newarr = csr_matrix(arr).tocsc()
print(newarr)
