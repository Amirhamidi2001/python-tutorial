# Python Strings

print("Hello")
print("Hello")

# Quotes Inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays

a = "Hello, World!"
print(a[1])

# Looping Through a String

for x in "banana":
    print(x)

# String Length

a = "Hello, World!"
print(len(a))

# Check String

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Check if NOT

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing Strings

b = "Hello, World!"
print(b[2:5])

# Slice From the Start

b = "Hello, World!"
print(b[:5])

# Slice To the End

b = "Hello, World!"
print(b[2:])

# Negative Indexing

b = "Hello, World!"
print(b[-5:-2])


# Modify Strings

# Upper Case

a = "Hello, World!"
print(a.upper())

# Lower Case

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

a = " Hello, World! "
print(a.strip())

# Replace String

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String

a = "Hello, World!"
print(a.split(","))

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format

"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

# F-Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Character

"""
txt = "We are the so-called "Vikings" from the north."
"""

# txt = "We are the so-called \"Vikings\" from the north."
txt = 'We are the so-called "Vikings" from the north.'
