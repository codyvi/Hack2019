from flask import Flask, render_template, request
import logging
import sys

import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index',methods=["GET","POST"])
def login():
    def db_query():
        _db = db.Database()
        counter = 0
        if request.method == "POST":
            sID = request.form["sId"]
            sPass = request.form["sPass"]
            res =_db.login(sID, sPass)
            print('Entrando...', file=sys.stdout)
            print(res, file=sys.stdout)

            return res
            

    res = db_query()

    if len(res) >= 1:
        return render_template('SesiónUsuario.html', result=res, content_type='application/json')
    else:
        return render_template('index.html', result=res, content_type='application/json')


            
