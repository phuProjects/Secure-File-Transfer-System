from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os #Access .env

# Laod varibles from.env into the Environment
load_dotenv()

# Get the encryption key from the environment and encode to bytes
key = os.getenv("ENCRYPTION_KEY").encode()
if key is None:
    raise ValueError("Encryption_Key not found in .env")

# Create a Fernet object with the key
fernet = Fernet(key)

# Message to encrypt (bytes)
message = b"Hello World!"

#Encrypt message
encrypted = fernet.encrypt(message)

# Print the encrypted message (in bytes)
print("Encrypted:", encrypted)
