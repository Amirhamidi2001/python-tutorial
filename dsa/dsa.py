# Python Data Structures and Algorithms (DSA)

# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

# List Methods
x = [9, 12, 7, 4, 11]

# Add element:
x.append(8)

# Sort list ascending:
x.sort()

# Create Algorithms
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print("Lowest value:", minVal)
