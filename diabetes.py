from flask import Flask, Blueprint, render_template, request, app, redirect, url_for
import pickle
import json
import numpy as np
import pandas as pd 
import sklearn
from flask import Response
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

diabetesp = Blueprint('diabetes', __name__)

@diabetesp.route("/diabetes")
def diabetes():
    return render_template('diabetes_predictor.html')


@diabetesp.route("/predict", methods=['POST'])
def diabetesproute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is:     ', data)
            res = dpredict_log(data)
            print('result is        ', res)
            return Response(res)
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ', e)
        return Response(e)

def dpredict_log(dict_pred):
    with open("diabetespredictorrandomforest.sav", 'rb') as f:
        model = pickle.load(f)

    data_df = pd.DataFrame(dict_pred, index=[1, ])
    dpredict = model.predict(data_df)
    if dpredict[0] == 1:
        result = 'Oops! You have DIABETES.'
    else:
        result = "Great! You DON'T have diabetes."
    return result

@diabetesp.route('/diabetespredict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        dprediction = dpredict_log(data)
        
        return render_template('diabetes_predictor.html', dprediction=dprediction)

if __name__ == '__main__':
	diabetesp.run(debug=True)