from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

with open('../../Q4files/.key.txt', 'rb') as f:
    key = f.read()
    
with open('../../Q4files/Encrypted4', 'rb') as f:
    raw_text = f.read() 


iv = raw_text[:AES.block_size]
ciphertext = raw_text[AES.block_size:]

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered_data = cipher.decrypt(ciphertext)

print(unpad(ciphered_data, AES.block_size).decode('utf-8').strip())
