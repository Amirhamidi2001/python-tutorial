# Python None

# NoneType
x = None
print(x)
print(type(x))

# Comparing to None
result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

# Comparing to None
result = None
if result is not None:
    print("Result is ready")
else:
    print("No result yet")

# True or False
print(bool(None))


# Functions returning None
def myfunc():
    x = 5


x = myfunc()
print(x)
