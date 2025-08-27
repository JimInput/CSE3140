import sys
import datetime
import subprocess

now = datetime.datetime.now()

# file opening
with open('../Q1/MostCommonPWs', 'r') as file:
    candidates = file.read().splitlines()

password = ""

for candidate in candidates:
    result = subprocess.run(['python3', '../Q1/Login.pyc', "SkyRedFalcon914", candidate], capture_output=True, text=True)
    print(f"User: SkyRedFalcon914 Pass: {candidate}")
    
    if result.stdout=='Login successful.\n':
        password = candidate
        break

print(now)
print(f"The password is: {password}")
print(datetime.datetime.now())
