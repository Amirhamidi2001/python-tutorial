# NumPy Array Indexing

# Access Array Elements
import numpy as np

arr = np.array([1, 2, 3, 4])

# Get the first element
print(arr[0])

# Get the second element
print(arr[1])

# Get third and fourth elements and add them
print(arr[2] + arr[3])

# Access 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Access the element on the first row, second column
print("2nd element on 1st row: ", arr[0, 1])

# Access the element on the 2nd row, 5th column
print("5th element on 2nd row: ", arr[1, 4])

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access the third element of the second array of the first array
print(arr[0, 1, 2])

# Negative Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Print the last element from the 2nd dim
print("Last element from 2nd dim: ", arr[1, -1])
