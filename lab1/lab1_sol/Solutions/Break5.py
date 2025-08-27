import sys
import datetime
import subprocess
import hashlib

start = datetime.datetime.now()

hash_to_user = dict()

# file opening
with open('../Q5/HashedPWs', 'r') as file:
    for userpass in file:
        user, hash_value = userpass.strip().split(",")
        hash_to_user[hash_value] = user

with open('../Q5/PwnedPWs100k', 'r') as file:
    candidates = file.read().splitlines()

username = ''
password = ''

for candidate in candidates:
    
    # random number added on to the end
    for i in range(0, 100):
        test_pswd = candidate
        
        # digits 00 - 09
        if i < 10:
            test_pswd = test_pswd + str(0) + str(i)
        # digits 10 - 99
        else:
            test_pswd = test_pswd + str(i)
            
        h = hashlib.sha256()
        h.update(bytes(test_pswd, 'utf-8'))
        hashed_guess = h.hexdigest()
        
        # check if we have hashed result already stored
        if hashed_guess in hash_to_user:
            result = subprocess.run(['python3', '../Q5/Login.pyc', hash_to_user[hashed_guess], test_pswd], capture_output=True, text=True)
            print(hash_to_user[hashed_guess], test_pswd)
            
            # then check to see if pass before hashing is correct.
            if result.stdout == 'Login successful.\n':
                username = hash_to_user[hashed_guess]
                password = test_pswd
                break
            
    if username != '':
        break

print(start)
print(f"User: {username} Pass: {password}")
print(datetime.datetime.now())
