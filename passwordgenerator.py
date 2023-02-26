import random
import string

def generate_password(length=12):
    # Define the character sets to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+"

    # Combine the character sets
    all_chars = lowercase + uppercase + digits + special_chars

    # Shuffle the characters and select a random subset of the desired length
    password = ''.join(random.sample(all_chars, length))

    return password

if __name__ == "__main__":
    password = generate_password()
    print("Your password is:", password)
