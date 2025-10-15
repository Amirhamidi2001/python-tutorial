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
mycursor = mydb.cursor(buffered=True)
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

# Select With a Filter
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Wildcard Characters
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Prevent SQL Injection
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Sort the Result
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# ORDER BY DESC
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Delete Record
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# Prevent SQL Injection
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql, adr)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# Update Table
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Prevent SQL Injection
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Limit the Result
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Start From Another Position
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Join Two or More Tables
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# LEFT JOIN
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

# RIGHT JOIN
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

# Delete a Table
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)

# Drop Only if Exist
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
