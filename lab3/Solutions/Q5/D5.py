from Crypto.Hash import MD5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

with open('../../Q5files/Encrypted5', 'rb') as f:
    raw_text = f.read() 
    
h = MD5.new()
with open('../../Q5files/R5.py', 'rb') as afile:
    buf = afile.read(128)
    while len(buf) > 0:
        h.update(buf)
        buf = afile.read(128)

key = h.digest()

iv = raw_text[:AES.block_size]
ciphertext = raw_text[AES.block_size:]

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered_data = cipher.decrypt(ciphertext)

print(unpad(ciphered_data, AES.block_size).decode('utf-8').strip())
