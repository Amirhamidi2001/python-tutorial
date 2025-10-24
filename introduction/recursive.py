# Python Recursion


# Recursion
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)


# Base Case and Recursive Case
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))


# Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


# Recursion with Lists
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])


my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest


my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))
