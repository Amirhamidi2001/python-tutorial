# Python MongoDB Create Database

import pymongo


# Creating a Database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Check if Database Exists
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

# Creating a Collection
mycol = mydb["customers"]

# Check if Collection Exists
print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")
