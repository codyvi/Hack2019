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
        if request.method == "POST":
            sID = request.form["sID"]
            sPass = request.form["sPass"]
            res =_db.login(sID, sPass)
            print('Entrando...', file=sys.stdout)

            return res
            

        else:
            print('No se encontro usuario', file=sys.stdout)
            
        res = db_query()
             
        return render_template('index.html', result=res, content_type='application/json')


            
