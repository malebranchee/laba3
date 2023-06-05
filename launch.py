from flask import Flask, request, render_template
from UserLogin import login_check

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

data = login_check()
@app.route('/form_login', methods=['POST', 'GET'])
def login():
    user_log = request.form['username']
    user_password = request.form['password']
    if user_log not in data:
        return render_template('index.html',
                               info='Invalid User')
    else:
        if data[user_log] != user_password:
            return render_template('index.html',
                                   info='Invalid Password')
        else:
            return render_template('processed.html',
                                   name=user_log)
 # Run flask in debug mode
if __name__ == '__main__':
    app.run()