def main():
    numbers_divisors_count = {}

    for _ in range(20):
        number = int(input("Enter a number: "))
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        numbers_divisors_count[number] = len(divisors)

    # Sort by number of divisors, then by number value
    sorted_items = sorted(
        numbers_divisors_count.items(), key=lambda item: (item[1], item[0])
    )

    print("Number with the most divisors:", sorted_items[-1])


if __name__ == "__main__":
    main()
