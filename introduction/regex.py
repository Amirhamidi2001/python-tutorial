# Python RegEx

import re


# Sample text
txt = "The rain in Spain"

# The findall() function
matches = re.findall(r"ai", txt)
print(matches)  # ['ai', 'ai']

matches = re.findall(r"Portugal", txt)
print(matches)  # []

# The search() function
match = re.search(r"\s", txt)
if match:
    print("The first white-space character is located in position:", match.start())

match = re.search(r"Portugal", txt)
print(match)  # None

# The split() function
parts = re.split(r"\s", txt)
print(parts)

parts = re.split(r"\s", txt, maxsplit=1)
print(parts)

# The sub() function
replaced = re.sub(r"\s", "9", txt)
print(replaced)

replaced = re.sub(r"\s", "9", txt, count=2)
print(replaced)

# Match object examples
match = re.search(r"ai", txt)
print(match)

match = re.search(r"\bS\w+", txt)
if match:
    print(match.span())
    print(match.string)
    print(match.group())
