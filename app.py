from flask import Flask, Blueprint, render_template, request, app, redirect, session,  url_for
from flask import Response
from flask_cors import CORS
import py
import pickle
import py
from sklearn.preprocessing import StandardScaler
import json
import numpy as np
import pandas as pd

from carprice import carprices
from mobileclassify import mobileclassifys
from studentg import studentgrd
from diabetes import diabetesp
from restaurant import restaurantr
from spamsms import spamsmsc
from moviegenre import moviegenrem

app = Flask(__name__)
CORS(app)
app.register_blueprint(carprices)
app.register_blueprint(mobileclassifys)
app.register_blueprint(studentgrd)
app.register_blueprint(diabetesp)
app.register_blueprint(restaurantr)
app.register_blueprint(spamsmsc)
app.register_blueprint(moviegenrem)
app.config['DEBUG'] = True

@app.route('/maindashboard')
@app.route('/')
def maindashboard():
    return render_template('Main_Dashboard.html')

@app.route('/myprofile')
def myprofile():
    return render_template('my_profile.html')

if __name__ == '__main__':
    app.run(debug=True)