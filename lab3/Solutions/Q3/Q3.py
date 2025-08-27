from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os

with open(F'../../Q3pk.pem', 'rb') as file:
    key = file.read()
    # .strip("-----BEGIN PUBLIC KEY-----").strip("-----END PUBLIC KEY-----").strip()

def verify_signature(key, data, sig_f):
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_f, 'rb') as f: 
        signature = f.read()
    return signer.verify(h, signature)

files = os.listdir('../../Q3files')

for executable in files:
    if executable.endswith('.exe'):
        with open(f'../../Q3files/{executable}', 'rb') as file:
            file_data = file.read()
            
        if (verify_signature(key, file_data, (f"../../Q3files/{executable}.sign"))):
            print(executable)
            

