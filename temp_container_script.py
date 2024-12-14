from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from hashlib import sha256
import requests
import os
import base64

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
    flag = "WLUG{1203}"

    # Encrypt the message
    encrypted_message = encrypt_message(flag, key)

    # Encode the encrypted message to Base64
    encoded_message = base64.b64encode(encrypted_message).decode('utf-8')

    # Write the Base64-encoded message to a text file
    with open("encrypted_message.txt", "w") as file:
        file.write(encoded_message)

    print("Encryption complete. Encrypted message saved to 'encrypted_message.txt'.")
