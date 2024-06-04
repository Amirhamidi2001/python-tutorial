# Python File Open

# File Handling

f = open("demofile.txt", "r")
print(f.read())

f = open("/home/lenovo/Documents/GitHub/python-tutorial/file/demofile.txt", "r")
print(f.read())

# Read Only Parts of the File

f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines

f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close Files

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Python File Write

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

# Create a New File

"""
f = open("myfile.txt", "x")
"""

f = open("myfile.txt", "w")

# Python Delete File

import os

os.remove("myfile.txt")

# Check if File exist:

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

# Delete Folder

os.rmdir("myfolder")
