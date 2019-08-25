from flask import Flask, render_template, request, Response, redirect, url_for
from camera import VideoCamera
import pyzbar.pyzbar as pyzbar 
import time
import json
import logging
import sys
from flask_jsglue import JSGlue

import db

app = Flask(__name__)
jsglue = JSGlue(app)

image = None

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

@app.route('/data')
def do_foo():
    messages = request.args['messages']  # counterpart for url_for()
    messages = session['messages']       # counterpart for session
    return render_template("dataShown.html", messages=json.loads(messages))

@app.route('/camera')
def camera():
    return render_template('Camera.html')

def check():
    return False

def gen(camera):
    while True:
        global image
        frame, image = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/qr_check')
def qrcheck():
    print("Llego")
    if int(round(time.time() * 1000)) % 5000 :
        decodedObjects = pyzbar.decode(image)
        if decodedObjects != [] :
            for obj in decodedObjects:
                messages = json.dumps({"main":obj.data.decode("utf-8")})
            return render_template("dataShown.html", messages=json.loads(messages))    
    return []
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
            
