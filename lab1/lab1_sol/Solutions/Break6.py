import sys
import datetime
import subprocess
import hashlib

start = datetime.datetime.now()

hash_to_user = dict()
user_to_salt = dict()
user_to_hash = dict()

# opening files
with open('../Q6/PwnedPWs100k', 'r') as file:
    candidates = file.read().splitlines()

with open('../Q6/gang', 'r') as file:
    users = file.read().splitlines()
    users.remove("SkyRedFalcon914")
    users.remove("StarSilverBear427")
    users.remove("SkySilverWolf337")
    users.remove("ForestPurpleFalcon522")
    users.remove("ForestGreenWolf607")

with open('../Q6/SaltedPWs', 'r') as file:
    for usersaltpass in file:
        user, salt, hash_value = usersaltpass.strip().split(',')
        # only checks people in the gang
        if user in users:
            hash_to_user[hash_value] = user
            user_to_salt[user] = salt
            user_to_hash[user] = hash_value
        
username = ''
password = ''
answer_username = ''
answer_password = ''
cracked = dict()


for user in user_to_salt:
    for candidate in candidates:
        for digit in range(10):
            # form password in the form h(salt + pass + number)
            real_password = candidate + str(digit)
            to_hash = user_to_salt[user] + real_password
            
            h = hashlib.sha256()
            h.update(bytes(to_hash, 'utf-8'))
            candidate_hash = h.hexdigest()
            
            print(f"{user} {real_password}")
            
            if candidate_hash == user_to_hash[user]:
                result = subprocess.run(['python3', '../Q6/Login.pyc', user, real_password], capture_output=True, text=True)
                if result.stdout=="Login successful.\n":
                    answer_username = user
                    answer_password = real_password
                    
                cracked[user] = real_password
                username = user
                password = real_password
                break
        if user in cracked.keys():
            break
    
# write found passwords to the out text file
with open("Break_6_out.txt", "w") as file:
    for user, candidate in cracked.items():
        file.write(f"User: {user} Pass: {candidate}\n")


print(start)
for user, candidate in cracked.items():
    print(f"User: {user} Pass: {candidate}")
print()
# The username of the person who I was able to log in with.
print(f"User: {answer_username}")
print(datetime.datetime.now())
