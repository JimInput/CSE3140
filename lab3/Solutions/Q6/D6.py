from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
from Crypto.Cipher import PKCS1_OAEP, AES
import os
import sys


with open(sys.argv[1], "rb") as f:
    shared_key = f.read()
    
files = [e for e in os.listdir() if e.endswith(".encrypted")]

for file in files:
    with open(file, 'rb') as f:
        encrypted_text = f.read()

    iv = encrypted_text[:AES.block_size]
    ciphertext = encrypted_text[AES.block_size:]

    cipher = AES.new(shared_key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    
    with open(file.replace(".encrypted", ""), 'w') as f:
        f.write(unpad(decrypted_data, AES.block_size).decode("utf-8").strip())
        
    os.remove(file)