from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import requests
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from hashlib import sha256
import os

# Static passphrase and key derivation
passphrase = b"Walchand_Linux_Users_Group"
key = sha256(passphrase).digest()  # 32-byte key for AES-256

def encrypt_message(plain_text, key):
    iv = os.urandom(16)  # Generate a random IV
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plain_text.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_message

if __name__ == "__main__":
    # Message to encrypt



# Configuration
    SERVER_URL = "http://127.0.0.1:5000/flag"  # Replace with your server's URL

    def fetch_flag():
        """
        Fetch the flag from the server.
        """
        try:
            response = requests.get(SERVER_URL)
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as e:
            print(f"Error fetching flag: {e}")
            return None

    if __name__ == "__main__":
        # Fetch the flag
        flag = fetch_flag()
        if flag:
            print(f"Fetched flag: {flag}")
        else:
            print("Failed to fetch the flag.")

    # flag = "WLUG{1203}"

    # Encrypt the message
    encrypted_message = encrypt_message(flag, key)

    # Write the encrypted message to a file
    with open("encrypted_message.bin", "wb") as file:
        file.write(encrypted_message)

    print("Encryption complete. Encrypted message saved to 'encrypted_message.bin'.")
