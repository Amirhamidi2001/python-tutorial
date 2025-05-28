# Python Arrays

cars = ["Ford", "Volvo", "BMW"]
print(cars)

car1, car2, car3 = cars
print(car1)
print(car2)
print(car3)

# Access the Elements of an Array
x = cars[0]
print(x)

cars[0] = "Toyota"
x = cars[0]
print(x)

# The Length of an Array
x = len(cars)
print(x)

# Looping Array Elements
for x in cars:
    print(x)

# Adding Array Elements
cars.append("Honda")
print(cars)

# Removing Array Elements
cars.pop(1)
print(cars)

cars.remove("Toyota")
print(cars)
