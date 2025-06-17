# Python User Input

import math


# User Input
print("Enter your name:")
name = input()
print(f"Hello {name}")

# Using prompt
name = input("Enter your name:")
print(f"Hello {name}")

# Multiple Inputs
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input Number
x = input("Enter a number:")

# find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

# Validate Input
y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")
