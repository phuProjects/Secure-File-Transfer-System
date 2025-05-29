from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os #Access .env


# Laod varibles from.env into the Environment.
load_dotenv()

# Get the encryption key from the environment and encode to bytes.
key = os.getenv("ENCRYPTION_KEY").encode()
if key is None:
    raise ValueError("Encryption_Key not found in .env")

# Create a Fernet object with the key.
fernet = Fernet(key)

#Function to encrypt message/file in bytes. 
def encrypt_message(bytes_data):
    return fernet.encrypt(bytes_data)

