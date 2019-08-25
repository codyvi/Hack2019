from flask import Flask, render_template, request, response
from camera import VideoCamera
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

@app.route('/camera')
def index():
    return render_template('Camera.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
            
