import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random password.

    Args:
        length: The desired length of the password.
        use_uppercase: Include uppercase letters.
        use_lowercase: Include lowercase letters.
        use_digits: Include digits.
        use_symbols: Include symbols.

    Returns:
        A randomly generated password as a string, or None if no character sets are selected.
    """

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None  # No character sets selected

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

        if password:
            print("Generated password:", password)
        else:
            print("Please select at least one character set.")
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")