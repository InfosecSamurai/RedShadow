from Crypto.Cipher import AES
import base64
import os

KEY = os.urandom(16)  # Generate a random encryption key

def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text

def encrypt(plain_text):
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode())
    return base64.b64encode(encrypted_text).decode()

def decrypt(encrypted_text):
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode().strip()
    return decrypted_text