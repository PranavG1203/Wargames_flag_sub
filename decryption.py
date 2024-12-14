from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from hashlib import sha256
import base64

# Static passphrase and key derivation
passphrase = b"Walchand_Linux_Users_Group"
key = sha256(passphrase).digest()  # 32-byte key for AES-256

def decrypt_message(encoded_message, key):
    # Decode the Base64-encoded message
    encrypted_message = base64.b64decode(encoded_message)

    # Extract the IV and the encrypted content
    iv = encrypted_message[:16]
    encrypted_content = encrypted_message[16:]

    # Decrypt the message
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_content) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    original_message = unpadder.update(decrypted_message) + unpadder.finalize()
    return original_message.decode('utf-8')

if __name__ == "__main__":
    # Read the Base64-encoded encrypted message from the text file
    with open("encrypted_message.txt", "r") as file:
        encoded_message = file.read().strip()

    # Decrypt the message
    try:
        decrypted_message = decrypt_message(encoded_message, key)
        print(f"Decrypted message: {decrypted_message}")
    except Exception as e:
        print(f"Decryption failed: {e}")
