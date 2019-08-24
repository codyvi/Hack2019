from flask import Flask, render_template, request
import logging
import sys

import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')