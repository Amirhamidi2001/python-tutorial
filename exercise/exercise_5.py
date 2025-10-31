def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisors(n):
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


# Input 10 numbers
numbers = [int(input()) for _ in range(10)]

# Build dictionary: number → count of prime divisors
prime_divisor_count = {n: sum(1 for d in divisors(n) if is_prime(d)) for n in numbers}

# Find the number with the highest prime divisor count (and highest number if tie)
result = max(prime_divisor_count.items(), key=lambda item: (item[1], item[0]))

print(result)
