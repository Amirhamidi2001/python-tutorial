# Python Dictionaries

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

# Dictionary Items
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
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.keys()
print(x)  # before the change

car["color"] = "white"
print(x)  # after the change

# Get Values
x = thisdict.values()
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.values()
print(x)  # before the change

car["year"] = 2020
print(x)  # after the change

car["color"] = "red"
print(x)  # after the change

# Get Items
x = thisdict.items()
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.items()
print(x)  # before the change

car["year"] = 2020
print(x)  # after the change

car["color"] = "red"
print(x)  # after the change

# Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print(thisdict)

# Update Dictionary
thisdict.update({"year": 2020})
print(thisdict)

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Update Dictionary
thisdict.update({"owner": "John"})
print(thisdict)

# Removing Items
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["color"]
print(thisdict)

"""
del thisdict
print(thisdict)
"""

thisdict.clear()
print(thisdict)

# Loop Through a Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020,
    "color": "red",
    "owner": "John",
}
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x, y)

# Copy a Dictionary
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
print(myfamily)

child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily = {"child1": child1, "child2": child2, "child3": child3}
print(myfamily)

# Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])
