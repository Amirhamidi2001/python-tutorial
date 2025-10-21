# Python Operators

# Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x % y)
print(x**y)

# Division in Python
print(x / y)
print(x // y)

# The Walrus Operator
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining Comparison Operators
x = 5

print(1 < x < 10)
print(1 < x and x < 10)

# Logical Operators
x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not (x > 3 and x < 10))

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

# Membership Operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

# Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

# Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

# Left-to-Right Evaluation
print(5 + 4 - 7 + 3)
