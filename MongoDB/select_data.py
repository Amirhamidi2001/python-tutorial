# Python MongoDB Find

import pymongo


# Conection to Database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Find One
x = mycol.find_one()
print(x)

# Find All
for x in mycol.find():
    print(x)

# Return Only Some Fields
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

for x in mycol.find({}, {"address": 0}):
    print(x)

# Filter the Result
myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Advanced Query
myquery = {"address": {"$gt": "S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Filter With Regular Expressions
myquery = {"address": {"$regex": "^S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Sort the Result
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

# Sort Descending
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)
