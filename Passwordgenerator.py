import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using random.choices()
    password = ''.join(random.choices(characters, k=length))
    return password

# Generate and print a random password of default length 12
print("Random Password:", generate_password())
