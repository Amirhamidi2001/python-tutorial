# Python Try Except

# Exception Handling
try:
    print(x)
except:
    print("An exception occurred")

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# Raise an exception
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
