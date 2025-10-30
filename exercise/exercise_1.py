from random import randint


def number_guessing_game():
    """Simple number guessing game where the computer guesses your number."""
    lower_bound, upper_bound = 1, 100

    while True:
        guess = randint(lower_bound, upper_bound)
        print(guess)
        answer = input("Enter 'd' if correct, 'b' if too low, or 'k' if too high: ")

        if answer == "d":
            print("You win!")
            break
        elif answer == "b":
            lower_bound = guess + 1
        elif answer == "k":
            upper_bound = guess - 1
        else:
            print("Invalid input. Please enter 'd', 'b', or 'k'.")


if __name__ == "__main__":
    number_guessing_game()
