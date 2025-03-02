# computer_guess_game.py (Computer's program)
import random

def computer_guess():
    """Computer guesses a number chosen by the user."""
    low = 1
    high = 100
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Could be high, they are equal
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")

if __name__ == "__main__":
    print("Think of a number between 1 and 100, and I will try to guess it.")
    computer_guess()