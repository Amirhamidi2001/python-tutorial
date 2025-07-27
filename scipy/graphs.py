# SciPy Graphs

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import (
    connected_components,
    dijkstra,
    floyd_warshall,
    bellman_ford,
    depth_first_order,
    breadth_first_order,
)


# Connected Components
arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
newarr = csr_matrix(arr)
print(connected_components(newarr))

# Dijkstra
arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_predecessors=True, indices=0))

# Floyd Warshall
arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors=True))

# Bellman Ford
arr = np.array([[0, -1, 2], [1, 0, 0], [2, 0, 0]])
newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors=True, indices=0))

# Depth First Order
arr = np.array([[0, 1, 0, 1], [1, 1, 1, 1], [2, 1, 1, 0], [0, 1, 0, 1]])
newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

# Breadth First Order
arr = np.array([[0, 1, 0, 1], [1, 1, 1, 1], [2, 1, 1, 0], [0, 1, 0, 1]])
newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))
