from flask import Flask, Blueprint, render_template, request, app, redirect, url_for
import pickle
import json
import numpy as np
import pandas as pd 
import sklearn
from flask import Response
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler

studentgrd = Blueprint('studentg', __name__)

@studentgrd.route("/studentg")
def studentg():
    return render_template('students_grad.html')

@studentgrd.route("/predict", methods=['POST'])
def studentgroute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is:     ', data)
            res = predict_log(data)
            print('result is        ', res)
            return Response(res)
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ', e)
        return Response(e)

# studentsandardScalar.sav StudentGradingmodelForPrediction.sav
def predict_log(dict_pred):                          
    with open("studentsandardScalar.sav", 'rb') as f:
        scalar = pickle.load(f)

    with open("StudentGradingmodelForPrediction.sav", 'rb') as f:
        model = pickle.load(f)

    data_df = pd.DataFrame(dict_pred, index=[1, ])
    scaled_data = scalar.transform(data_df)
    predict = model.predict(scaled_data)
    if predict[0] == 0:
        result = 'Very Poor'
    elif predict[0] == 1:
        result = 'Poor'
    elif predict[0] == 2:
        result = 'Below Average'
    elif predict[0] == 3:
        result = 'Average'
    elif predict[0] == 4:
        result = 'Very Good'
    else:
        result = 'Excellent'

    return result

@studentgrd.route("/spridict", methods=['POST'])
def spridict():
    if request.method == "POST":
        cse_math_score = request.form['cse_math_score']
        eee_score = request.form['eee_score']
        cse_deploy_score = request.form['cse_deploy_score']
        math_score = request.form['math_score']

        sprediction = predict_log(np.array([[cse_math_score, eee_score, cse_deploy_score, math_score]]))

        return render_template('students_grad.html', sprediction="Your Result is {}".format(sprediction))
    else:
        return render_template('students_grad.html')



if __name__ == '__main__':
    studentgrd.run(debug=True)
