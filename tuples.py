# Python Tuples

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(type(thistuple))
print(thistuple)
print(len(thistuple))

# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
# thistuple = "apple"
# print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
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
print(thistuple[-4:-1])

# Check if Item Exists

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values

x = ("apple", "banana", "cherry")
print(x)

y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")
print(thistuple)

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

# Add tuple to a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) """ this will raise an error because the tuple no longer exists """

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
print(fruits)

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
print(fruits)

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop Through the Index Numbers

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Using a While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Join Two Tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple Methods

x = mytuple.count("apple")
print(x)

x = mytuple.index("apple")
print(x)
