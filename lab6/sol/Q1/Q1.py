from flask import Flask, render_template, request, jsonify, url_for, redirect, make_response

app = Flask(__name__)

NETID = "jpj22002"
LAST_NAME = "Padilla"
VM_IP = "10.13.6.152"

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        netid = request.form.get('netid')

        resp = make_response(redirect(url_for('index')))

        resp.set_cookie('Q1B1', netid)
        resp.set_cookie('Q1B2', LAST_NAME, path='/Q1B2')
        resp.set_cookie('Q1B3', VM_IP, httponly=True, samesite='Strict')
        return resp

    username = request.cookies.get('Q1B1')
    return render_template('index.html', username=username)


@app.route('/Q1B2/')
def q1b2():
    return render_template('q1b2.html')  

if __name__ == '__main__':
    app.run(debug=True)


