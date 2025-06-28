# Python File Open

import os

# File Handling
f = open("demofile.txt")
print(f.read())

f = open("demofile.txt", "rt")
print(f.read())

f = open("/home/leno/Documents/GitHub/python-tutorial/filehandling/demofile.txt")
print(f.read())

# Using the with statement
with open("demofile.txt") as f:
    print(f.read())

# Close Files
f = open("demofile.txt")
print(f.readline())
f.close()

# Read Only Parts of the File
with open("demofile.txt") as f:
    print(f.read(10))

# Read Lines
with open("demofile.txt") as f:
    print(f.readline())

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

with open("demofile.txt") as f:
    for x in f:
        print(x)

# Write to an Existing File
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

# open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())

with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())

# Create a New File
f = open("myfile.txt", "x")

# Delete a File
os.remove("myfile.txt")

# Check if File exist:
f = open("myfile.txt", "x")

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

# Delete Folder
"""
os.rmdir("myfolder") 
"""
