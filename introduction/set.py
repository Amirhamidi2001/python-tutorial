# Python Sets

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True = 1
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False = 0
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)
print("banana" not in thisset)

# Add Items
thisset.add("orange")
print(thisset)

# Add Sets
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Item
thisset.remove("banana")
print(thisset)

"""
Note: If the item to remove does not exist, remove() will raise an error.
"""

thisset.discard("orange")
print(thisset)

"""
Note: If the item to remove does not exist, discard() will NOT raise an error.
"""

x = thisset.pop()
print(thisset)
print(x)


thisset.clear()
print(thisset)

# del thisset
# print(thisset)

# Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Join Sets

# Union
set1 = {"a", "b", "c", "e"}
set2 = {1, 2, 3, 4}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

# Join Multiple Sets
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2 | set3 | set4
print(myset)

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)

# Difference
set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)

set1.difference_update(set2)
print(set1)

# Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2
print(set3)

set1.symmetric_difference_update(set2)
print(set1)

# Python frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
