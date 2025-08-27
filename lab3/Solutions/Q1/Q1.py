# result = subprocess.run(['python3', '../Q1/Login.pyc', "SkyRedFalcon914", candidate], capture_output=True, text=True)
# result.stdout=='Login successful.\n'
import os
import subprocess


files = os.listdir('../../Q1files')

with open('../../Q1hash.txt') as file:
    hash_text = file.read().strip()
    
for executable in files:
    with open(f'../../Q1files/{executable}') as file:
        result = subprocess.run(['sha256sum', f'../../Q1files/{executable}'], capture_output=True, text=True)
        
    test_hash = result.stdout.split(" ")[0].strip()
    
    if test_hash == hash_text:
        print(f"{executable}")
        

    