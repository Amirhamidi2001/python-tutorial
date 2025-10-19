# Python MongoDB Delete Document

import pymongo


# Conection to Database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Delete Document
myquery = {"address": "Mountain 21"}
x = mycol.delete_one(myquery)
print(x.deleted_count, " document deleted.")

# Delete Many Documents
myquery = {"address": {"$regex": "^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# Delete All Documents in a Collection
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# Delete Collection
x = mycol.drop()
