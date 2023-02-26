from cryptography.fernet import Fernet

# Generate a random key
key = Fernet.generate_key()

# Define a plaintext message to encrypt
plaintext = b"This is a secret message."

# Create a Fernet instance using the key
f = Fernet(key)

# Encrypt the plaintext message
ciphertext = f.encrypt(plaintext)

# Print the encrypted message and the key
print("Encrypted message:", ciphertext)
print("Key:", key)
