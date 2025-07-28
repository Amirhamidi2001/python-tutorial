# SciPy Spatial Data

import numpy as np
from scipy.spatial import Delaunay, ConvexHull, KDTree, distance
import matplotlib.pyplot as plt


# Triangulation
points = np.array([[2, 4], [3, 4], [3, 0], [2, 2], [4, 1]])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color="r")
plt.show()

# Convex Hull
points = np.array(
    [[2, 4], [3, 4], [3, 0], [2, 2], [4, 1], [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]]
)
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:, 0], points[:, 1])

for simplex in hull_points:
    plt.plot(points[simplex, 0], points[simplex, 1], "k-")

plt.show()

# KDTrees
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

# Euclidean Distance
p1 = (1, 0)
p2 = (10, 2)
res = distance.euclidean(p1, p2)
print(res)

# Cityblock Distance (Manhattan Distance)
p1 = (1, 0)
p2 = (10, 2)
res = distance.cityblock(p1, p2)
print(res)

# Cosine Distance
p1 = (1, 0)
p2 = (10, 2)
res = distance.cosine(p1, p2)
print(res)

# Hamming Distance
p1 = (True, False, True)
p2 = (False, True, True)
res = distance.hamming(p1, p2)
print(res)
