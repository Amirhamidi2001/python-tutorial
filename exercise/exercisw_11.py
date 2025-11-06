import re
import secrets
import string


def generate_password(
    length: int = 16,
    nums: int = 1,
    special_chars: int = 1,
    uppercase: int = 1,
    lowercase: int = 1,
):
    """Generate a secure password with specified constraints."""

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    while True:
        password = "".join(secrets.choice(all_characters) for _ in range(length))

        constraints = [
            (nums, r"\d"),
            (special_chars, rf"[{re.escape(symbols)}]"),
            (uppercase, r"[A-Z]"),
            (lowercase, r"[a-z]"),
        ]

        if all(
            count <= len(re.findall(pattern, password))
            for count, pattern in constraints
        ):
            break

    return password


if __name__ == "__main__":
    new_password = generate_password()
    print("Generated password:", new_password)
