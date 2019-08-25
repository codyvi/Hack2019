from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
import bcrypt
import logging
import sys

import db

app = Flask(__name__)

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'residence'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login',methods=["GET","POST"])
def login():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            sID = request.form["sID"]
            sPass = request.form["sPass"]
            
