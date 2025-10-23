# Python If Statement

# Python Conditions and If statements
a = 33
b = 200
c = 500

if b > a:
    print("b is greater than a")

# Using Variables in Conditions
is_logged_in = True
if is_logged_in:
    print("Welcome back!")

# The Elif Keyword
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Multiple Elif Statements
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# When to Use Elif
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

# The Else Keyword
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Else Without Elif
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Else as Fallback
username = "Emil"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")

# Short Hand If
if a > b:
    print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

# Assign a Value With If ... Else
bigger = a if a > b else b
print("Bigger is", bigger)

# Multiple Conditions on One Line
print("A") if a > b else print("=") if a == b else print("B")

# Practical Examples
max_value = a if a > b else b
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# The and Operator
if b > a and c > a:
    print("Both conditions are True")

# The or Operator
if b > a or a > c:
    print("At least one of the conditions is True")

# The not Operator
if not b > a:
    print("a is NOT greater than b")

# Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

# Using Parentheses for Clarity
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

# More Examples
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")

score = 85

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")

# Nested If Statements
if b > 10:
    print("Above ten,")
    if b > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# How Nested If Works
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

# Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

# Nested If vs Logical Operators
temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")

if temperature > 20 and is_sunny:
    print("Perfect beach weather!")

username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")

score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade or below")

# The pass Statement
if b > a:
    pass

# pass in Development
if age < 18:
    pass
else:
    print("Access granted")

# pass with Multiple Conditions
value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass  # Zero case - no action needed
else:
    print("Positive value")


# pass in Other Contexts
def calculate_discount(price):
    pass
