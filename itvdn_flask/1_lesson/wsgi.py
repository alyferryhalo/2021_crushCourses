# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/login/')
def login():
    return render_template('login.html', title='LogIn')

if __name__ == "__main__":
    app.run()