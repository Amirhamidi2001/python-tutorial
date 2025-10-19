# Python MongoDB Update

import pymongo

# Conection to Database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Update Collection
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)

# print "customers" after the update:
for x in mycol.find():
    print(x)

# Update Many
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"name": "Minnie"}}
x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

# Limit the Result
myresult = mycol.find().limit(5)

# print the result:
for x in myresult:
    print(x)
