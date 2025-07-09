# Random Numbers in NumPy

from numpy import random


# Generate Random Number
x = random.randint(100)
print(x)

# Generate Random Float
x = random.rand()
print(x)

# Generate Random Array
x = random.randint(100, size=(5))
print(x)

x = random.randint(100, size=(3, 5))
print(x)

# Floats
x = random.rand(5)
print(x)

x = random.rand(3, 5)
print(x)

# Generate Random Number From Array
x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
