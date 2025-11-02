def verify_card_number(card_number):
    """Validate a credit card number using the Luhn algorithm."""
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    """Prompt for a card number and print whether it is valid."""
    card_number = input("Enter card number: ").strip()
    cleaned = card_number.replace("-", "").replace(" ", "")
    print("VALID!" if verify_card_number(cleaned) else "INVALID!")


if __name__ == "__main__":
    main()
