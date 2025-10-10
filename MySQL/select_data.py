# Python MySQL Select From

# Select From a Table
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

mydb = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, password=DB_PASS, database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Selecting Columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Using the fetchone() Method
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()

print(myresult)
