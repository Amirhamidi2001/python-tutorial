# Python range

# Call range() With One Argument
x = range(10)
print(list(x))

# Call range() With Two Arguments
x = range(3, 10)
print(list(x))

# Call range() With Three Arguments
x = range(3, 10, 2)
print(list(x))

# Using ranges
for i in range(10):
    print(i)

# Using List to Display Ranges
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

# Slicing Ranges
r = range(10)
print(r[2])
print(r[:3])

# Membership Testing
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# Length
r = range(0, 10, 2)
print(len(r))
