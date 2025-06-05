#decrypt.py
from cryptography.fernet import Fernet 
from dotenv import load_dotenv
import os

#Load encryption key
load_dotenv()
key = os.getenv("ENCRYPTION_KEY").encode()
fernet = Fernet(key)

def decrypt_data(encrypted_data):
    return fernet.decrypt(encrypted_data)