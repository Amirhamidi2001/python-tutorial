# Python Numbers

x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(x))
print(type(y))
print(type(z))

# Int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12e4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number

import random

print(random.randrange(1, 10))

# Specify a Variable Type

# Integers:
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

# Floats:
x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

# Strings:
x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
