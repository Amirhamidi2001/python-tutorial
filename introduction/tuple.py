# Tuple Operations

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
print(len(thistuple))

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = "apple"
print(type(thistuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# type() to check the tuple type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Tuple Items
print(thistuple[1])

# Negative Indexing
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

# Range of Negative Indexes
print(thistuple[-4:-1])

# Check if Item Exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values - Convert to List and back
x = ("apple", "banana", "cherry")
x = tuple(["kiwi" if item == "banana" else item for item in x])
print(x)

# Add Items - By concatenation
thistuple = ("apple", "banana", "cherry")
thistuple += ("orange",)
print(thistuple)

# Remove Items - By converting to list, modifying, and converting back
thistuple = ("apple", "banana", "cherry")
thistuple = tuple([item for item in thistuple if item != "apple"])
print(thistuple)

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print(green, yellow, red)

# Using Asterisk* for Unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
green, yellow, *red = fruits
print(green, yellow, red)

# Loop Through a Tuple
for item in thistuple:
    print(item)

# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Tuple count() Method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# Tuple index() Method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
