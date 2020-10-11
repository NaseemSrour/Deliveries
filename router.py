from flask import Flask
from flask import render_template
from flask import request
import talk_to_db
import json

app = Flask(__name__)

@app.route('/aa', methods=['POST', 'GET'])
def aa():
    return 'aaaa'

@app.route('/add_new_item', methods=['POST', 'GET'])
def add_new_item():
    error = None
    if request.method == 'POST':
        if(valid_login(request.form['username'], request.form['password'])):
            return talk_to_db.add_item(request.form['item'])
        else:
            error = 'Login failed!'
    return render_template('login.html', error=error) # this is exected if it's a GET request

'''
To access parameters submitted in the URL (?key=value) you can
use the args attribute:

searchword = request.args.get('key', '')

'''

def valid_login(username, password):
    return True

