from flask import Flask, render_template, request, Response
from camera import VideoCamera
import pyzbar.pyzbar as pyzbar
import time
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

@app.route('/camera')
def camera():
    return render_template('Camera.html')

def gen(camera):
    while True:
        frame, image = camera.get_frame()
        if int(round(time.time() * 1000)) % 5000 :
            decodedObjects = pyzbar.decode(image)
            if decodedObjects != [] :
                for obj in decodedObjects:
                    print(obj.data)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
            
