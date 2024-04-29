# Python Dictionaries

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
print(thisdict["brand"])

# Duplicates Not Allowed

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)

# Dictionary Length

print(len(thisdict))

# Dictionary Items - Data Types

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(thisdict)

# type()

print(type(thisdict))

# The dict() Constructor

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# Accessing Items

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

# Get Keys

x = thisdict.keys()
print(x)  # before the change

thisdict["color"] = "white"
print(x)  # after the change

# Get Values

x = thisdict.values()
print(x)  # before the change

thisdict["year"] = 2020
print(x)  # after the change

# Get Items

x = thisdict.items()
print(x)

# Example

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.items()

print(x)  # before the change

car["year"] = 2020
car["color"] = "red"

print(x)  # after the change

# Check if Key Exists

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

thisdict["year"] = 2018
print(thisdict)

# Update Dictionary

thisdict.update({"year": 2020})
print(thisdict)

# Adding Items

thisdict["color"] = "red"
print(thisdict)

# Update Dictionary

thisdict.update({"color": "black"})
print(thisdict)

# Removing Items

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["year"]
print(thisdict)

# del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

thisdict.clear()
print(thisdict)

# Loop Through a Dictionary

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}

print(thisdict)
for x in thisdict:
    print(x)

print(thisdict)
for x in thisdict:
    print(thisdict[x])

print(thisdict)
for x in thisdict.values():
    print(x)

print(thisdict)
for x in thisdict.keys():
    print(x)

print(thisdict)
for x, y in thisdict.items():
    print(x, y)

# Copy a Dictionary

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries

myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
for x, y in myfamily.items():
    print(x, y)

child1 = {"name": "Emil", "year": 2004}

child2 = {"name": "Tobias", "year": 2007}

child3 = {"name": "Linus", "year": 2011}

myfamily = {"child1": child1, "child2": child2, "child3": child3}

for x, y in myfamily.items():
    print(x, y)

# Access Items in Nested Dictionaries

print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])

# Dictionary Methods

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
