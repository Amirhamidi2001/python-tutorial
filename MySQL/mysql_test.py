# Python MySQL Create Database
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

mydb = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS)
print(mydb)

# Creating a Database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
