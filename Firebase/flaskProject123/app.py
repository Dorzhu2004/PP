
import flask
import pyrebase
from flask import Flask, render_template, url_for, request, redirect


config = {
  'apiKey': "AIzaSyCEcNO07LoUe8mVMYuX0lRHMd1x3i_UyI8",
  'authDomain': "pppp-19566.firebaseapp.com",
  'databaseURL': "https://pppp-19566-default-rtdb.firebaseio.com",
  'storageBucket': "pppp-19566.appspot.com",
}

firebase = pyrebase.initialize_app(config)



app = Flask(__name__)

@app.route('/')
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    return render_template('auth.html', crt=url_for('create'), main=url_for('main'))

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template('create.html')


def newacc(email,password):
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email, password)

def sign(email,password):
    email=request.form.get('email')
    password=request.form.get('password')
    login=auth.sign_in_with_email_and_password(email, password)
    main()

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html', less=url_for('lessons'), obs=url_for('observations'), rep=url_for('reversP'), rev=url_for('revers'), inc=url_for('incorrect'))

@app.route('/lessons')
def lessons():
    return render_template('1.html', ex=url_for('main'))

@app.route('/observations')
def observations():
    return render_template('2.html', ex=url_for('main'))
@app.route('/reversP')
def reversP():
    return render_template('3.html', ex=url_for('main'))
@app.route('/revers')
def revers():
    return render_template('4.html', ex=url_for('main'))
@app.route('/incorrect')
def incorrect():
    return render_template('5.html', ex=url_for('main'))

if __name__ == '__main__':
    app.run()

def newacc():
    email = input('Email: ')
    password = input('Password: ')
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email, password)
newacc()

