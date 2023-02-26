from cryptography.fernet import Fernet
import os

# Function to generate a new key
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Function to load an existing key
def load_key():
    return open('key.key', 'rb').read()

# Function to encrypt a message using a key
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message using a key
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# Example usage
if __name__ == "__main__":
    if not os.path.exists('key.key'):
        generate_key()

    key = load_key()
    message = "This is a secret message"
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")
