from flask import Flask, render_template, request, redirect, url_for, session
import logging
import sys

import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
