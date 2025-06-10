# Python Modules

# Use a Module
import platform

import mymodule
import mymodule as mx
from mymodule import person1

mymodule.greeting("Amir")

# Variables in Module
a = mymodule.person1["name"]
print(a)

# Naming a Module
a = mx.person1["age"]
print(a)

# Built-in Modules
x = platform.system()
print(x)

# Using the dir() Function
x = dir(platform)
print(x)

# Import From Module
print(person1["age"])
