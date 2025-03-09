from Crypto.Cipher import AES
import base64
import os
import logging

logging.basicConfig(filename="encryption.log", level=logging.INFO)
logging.info("Initializing encryption module...")

KEY = os.urandom(16)

def pad(text):
    padding_length = 16 - (len(text) % 16)
    padding = chr(padding_length) * padding_length
    return text + padding

def unpad(text):
    padding_length = ord(text[-1])
    return text[:-padding_length]

def encrypt(plain_text):
    try:
        cipher = AES.new(KEY, AES.MODE_ECB)
        padded_text = pad(plain_text)
        encrypted_text = cipher.encrypt(padded_text.encode())
        return base64.b64encode(encrypted_text).decode()
    except Exception as e:
        logging.error(f"Error encrypting text: {e}")
        raise

def decrypt(encrypted_text):
    try:
        cipher = AES.new(KEY, AES.MODE_ECB)
        decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode()
        return unpad(decrypted_text)
    except Exception as e:
        logging.error(f"Error decrypting text: {e}")
        raise

def save_key_to_file(key_file="encryption_key.key"):
    try:
        with open(key_file, "wb") as file:
            file.write(KEY)
        logging.info(f"Encryption key saved to {key_file}")
    except Exception as e:
        logging.error(f"Error saving encryption key: {e}")
        raise

def load_key_from_file(key_file="encryption_key.key"):
    try:
        with open(key_file, "rb") as file:
            key = file.read()
        logging.info(f"Encryption key loaded from {key_file}")
        return key
    except Exception as e:
        logging.error(f"Error loading encryption key: {e}")
        raise

if __name__ == "__main__":
    plain_text = "This is a secret message."
    encrypted_text = encrypt(plain_text)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")