from Crypto.PublicKey import RSA

# define ECC as eliptical curve p256
key = RSA.generate(bits=2048)

# public key
with open('../e.key', 'wb') as f:
    data = key.public_key().export_key()
    f.write(data)
    
# private key
with open('../d.key', 'wb') as f:
    data = key.export_key()
    f.write(data)