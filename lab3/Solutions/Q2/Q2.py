import os
from Crypto.Hash import SHA256


files = os.listdir('../../Q2files')

with open('../../Q2hash.txt') as file:
    hash_text = file.read().strip()
    
for executable in files:
    with open(f'../../Q2files/{executable}', 'rb') as file:
        file_data = file.read()
        test_hash = SHA256.new(file_data).hexdigest()
        
    
    if test_hash == hash_text:
        print(f"{executable}")
        

    