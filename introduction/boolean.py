# Python Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass:
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean


def myFunction():
    return True


print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))
