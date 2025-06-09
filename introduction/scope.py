# Python Scope


# Local Scope
def myfunc():
    x = 100
    print(x)


myfunc()


# Function Inside Function
def myfunc():
    x = 200

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# Global Scope
x = 300


def myfunc():
    print(x)


myfunc()

print(x)

# Naming Variables
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)


# Global Keyword
def myfunc():
    global x
    x = 400


myfunc()

print(x)


# Nonlocal Keyword
def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"

    myfunc2()
    return x


print(myfunc1())
