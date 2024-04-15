# Python Lists

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items

print(thislist[1])

# Allow Duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length

print(len(thislist))

# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1, list2, list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# type

print(type(thislist))

# The list() Constructor

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# Python - Access List Items

print(thislist[1])
# Note: The first item has index 0.

# Negative Indexing

print(thislist[-1])

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

# Range of Negative Indexes

print(thislist[-4:-1])

# Check if Item Exists

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# Python - Change List Items

# Change Item Value

thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

# Python - Add List Items

thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Python - Remove List Items

thislist.remove("orange")
print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)

# del thislist
# The del keyword can also delete the list completely.

# Clear the List

# thislist.clear()
# print(thislist)

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
