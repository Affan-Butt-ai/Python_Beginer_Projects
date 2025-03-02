# user_guess_game.py (User's program)
import random

def user_guess():
    """User guesses a number chosen by the computer."""
    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")

if __name__ == "__main__":
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    user_guess()