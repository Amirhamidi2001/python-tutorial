# Python Sets

# Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the Length of a Set

print(len(thisset))

# type()

print(type(thisset))

# Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# The set() Constructor

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# Access Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("apple" in thisset)
print("banana" not in thisset)

# Add Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Item

thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
"""

# Loop Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Join Sets

# Union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}

set4 = set1.union(set2)
print(set4)

set5 = set1 | set2
print(set5)

myset = set1.union(set2, set3)
print(myset)

myset2 = set1 | set2 | set3
print(myset2)

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

# Use & to join two sets:

set3 = set1 & set2
print(set3)

set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

set4 = set1 - set2
print(set4)

set1.difference_update(set2)
print(set1)

# Symmetric Differences

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set4 = set1 ^ set2
print(set4)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# add() 	  	Adds an element to the set
# clear() 	  	Removes all the elements from the set
# copy() 	  	Returns a copy of the set
# difference() 	- 	Returns a set containing the difference between two or more sets
# difference_update() 	-= 	Removes the items in this set that are also included in another, specified set
# discard() 	  	Remove the specified item
# intersection() 	& 	Returns a set, that is the intersection of two other sets
# intersection_update() 	&= 	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() 	  	Returns whether two sets have a intersection or not
# issubset() 	<= 	Returns whether another set contains this set or not
#   	< 	Returns whether all items in this set is present in other, specified set(s)
# issuperset() 	>= 	Returns whether this set contains another set or not
#   	> 	Returns whether all items in other, specified set(s) is present in this set
# pop() 	  	Removes an element from the set
# remove() 	  	Removes the specified element
# symmetric_difference() 	^ 	Returns a set with the symmetric differences of two sets
# symmetric_difference_update() 	^= 	Inserts the symmetric differences from this set and another
# union() 	| 	Return a set containing the union of sets
# update() 	|= 	Update the set with the union of this set and others
