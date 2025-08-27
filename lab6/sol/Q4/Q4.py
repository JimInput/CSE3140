from flask import Flask, render_template, request, jsonify, url_for, redirect, make_response

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')