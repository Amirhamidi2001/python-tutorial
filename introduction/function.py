# Python Functions


# Creating a Function
def greet():
    print("Hello from a function")


greet()


# Return Values
def get_greeting():
    return "Hello from a function"


message = get_greeting()
print(message)

print(get_greeting())


# The pass Statement
def my_function():
    pass


# Arguments
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters vs Arguments
def my_function(name):  # name is a parameter
    print("Hello", name)


my_function("Emil")  # "Emil" is an argument


# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# Default Parameter Values
def my_function(name="friend"):
    print("Hello", name)


my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


def my_function(country="Norway"):
    print("I am from", country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Keyword Arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)


my_function(animal="dog", name="Buddy")
my_function(name="Buddy", animal="dog")
my_function("dog", "Buddy")
my_function("Buddy", "dog")


# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)


my_function("dog", name="Buddy", age=5)


# Passing Different Data Types
def my_function(fruits):
    for fruit in fruits:
        print(fruit)


my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])


my_person = {"name": "Emil", "age": 25}
my_function(my_person)


# Return Values
def my_function(x, y):
    return x + y


result = my_function(5, 3)
print(result)


# Returning Different Data Types
def my_function():
    return ["apple", "banana", "cherry"]


fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def my_function():
    return (10, 20)


x, y = my_function()
print("x:", x)
print("y:", y)


# Positional-Only Arguments
def my_function(name, /):
    print("Hello", name)


my_function("Emil")


# Keyword-Only Arguments
def my_function(*, name):
    print("Hello", name)


my_function(name="Emil")


# Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    return a + b + c + d


result = my_function(5, 10, c=15, d=20)
print(result)

# Python *args and **kwargs
# *args and **kwargs


# Arbitrary Arguments - *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# What is *args?
def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)


my_function("Emil", "Tobias", "Linus")


# Using *args with Regular Arguments
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)


my_function("Hello", "Emil", "Tobias", "Linus")


# Practical Example with *args
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(my_function(3, 7, 2, 9, 1))


# Arbitrary Keyword Arguments - **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# What is **kwargs?
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)


my_function(name="Tobias", age=30, city="Bergen")


# Using **kwargs with Regular Arguments
def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)


my_function("emil123", age=25, city="Oslo", hobby="coding")


# Combining *args and **kwargs
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")


# Unpacking Arguments
def my_function(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
result = my_function(*numbers)  # Same as: my_function(1, 2, 3)
print(result)


# Unpacking Dictionaries with **
def my_function(fname, lname):
    print("Hello", fname, lname)


person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)  # Same as: my_function(fname="Emil", lname="Refsnes")
