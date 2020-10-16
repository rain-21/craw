# -*- CODING = utf-8 -*-
# @TIME :  19:45
# @Author ： hwy
# @File : app.py
# @Software : PyCharm 19:45
from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run(debug=True)