# Python Lists

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# type()

print(type(thislist))

# List Length

print(len(thislist))

# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# The list() Constructor

thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thislist)

# Access Items

print(thislist[1])

# Negative Indexing

print(thislist[-1])

# Range of Indexes

print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

# Range of Negative Indexes

print(thislist[-4:-1])

# Check if Item Exists

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change Item Value

thislist[2] = "blackcurrant"
print(thislist)

# Change a Range of Item Values

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["banana"]
print(thislist)

# Insert Items

thislist.insert(2, "blackcurrant")
print(thislist)

# Append Items

thislist.append("cherry")
print(thislist)

# Extend List

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item

thislist.remove("banana")
print(thislist)

# Remove Specified Index

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[1]
print(thislist)

# Clear the List
"""
thislist.clear()
del thislist 
"""

# Loop Through a List

for x in thislist:
    print(x)

# Loop Through the Index Numbers

for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension

[print(x) for x in thislist]

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "e" in x]
print(newlist)

# Condition

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["hello" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Customize Sort Function


def myfunc(n):
    return abs(n - 50)


thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List

# Use the copy() method

mylist = thislist.copy()
print(mylist)

# Use the list() method

mylist = list(thislist)
print(mylist)

# Use the slice Operator

mylist = thislist[:]
print(mylist)

# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
