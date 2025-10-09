# Python MySQL Insert Into Table

# Insert Into Table
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

# Insert Into Table
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Insert Multiple Rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ("Peter", "Lowstreet 4"),
    ("Amy", "Apple st 652"),
    ("Hannah", "Mountain 21"),
    ("Michael", "Valley 345"),
    ("Sandy", "Ocean blvd 2"),
    ("Betty", "Green Grass 1"),
    ("Richard", "Sky st 331"),
    ("Susan", "One way 98"),
    ("Vicky", "Yellow Garden 2"),
    ("Ben", "Park Lane 38"),
    ("William", "Central st 954"),
    ("Chuck", "Main Road 989"),
    ("Viola", "Sideway 1633"),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

# Get Inserted ID
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
