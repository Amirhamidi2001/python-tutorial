# Python If ... Else

# Python Conditions and If statements
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Indentation
"""
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error 
"""

# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If
if a > b:
    print("a is greater than b")

# Short Hand If ... Else
print("A") if b > a else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
if a > b or a > c:
    print("At least one of the conditions is True")

# Not
if not a > c:
    print("a is NOT greater than c")

# Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
if b > a:
    pass
