from flask import Flask, Blueprint, render_template, request, app, redirect, url_for
import pickle
import json
import numpy as np
import pandas as pd 
import sklearn
from flask import Response
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler

mobileclassifys = Blueprint('mobileclassify', __name__)

@mobileclassifys.route("/mobileclassify")
def mobileprice():
    return render_template('mobile_classify.html')

@mobileclassifys.route("/predict", methods=['POST'])
def mobileroute():
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

#mobilepricesandardScalar.sav mobilepricemodelForPrediction.sav
def predict_log(dict_pred):
    with open("mobilepricesandardScalar.sav", 'rb') as f:
        scalar = pickle.load(f)

    with open("mobilepricemodelForPrediction.sav", 'rb') as f:
        model = pickle.load(f)

    data_df = pd.DataFrame(dict_pred, index=[1, ])
    scaled_data = scalar.transform(data_df)
    predict = model.predict(scaled_data)
    if predict[0] == 0:
        result = 'a Low Budget'
    elif predict[0] == 1:
        result = 'a Mid Budget'
    elif predict[0] == 2:
        result = 'a Mid-High Budget'
    else:
        result = 'an Expensive'
    return result

@mobileclassifys.route("/mpridict", methods=['POST'])
def pridict():
    if request.method == "POST":
        battery_power = request.form['battery_power']
        bluetooth = request.form['bluetooth']
        clock_speed = request.form['clock_speed']
        dual_sim = request.form['dual_sim']
        fc = request.form['fc']
        four_g = request.form['four_g']
        int_memory = request.form['int_memory']
        m_dep = request.form['m_dep']
        mobile_wt = request.form['mobile_wt']
        n_cores = request.form['n_cores']
        pc = request.form['pc']
        px_height = request.form['px_height']
        px_width = request.form['px_width']
        ram = request.form['ram']
        sc_h = request.form['sc_h']
        sc_w = request.form['sc_w']
        talk_time = request.form['talk_time']
        three_g = request.form['three_g']
        touch_screen = request.form['touch_screen']
        wifi = request.form['wifi']

        mprediction = predict_log(np.array([[battery_power, bluetooth, clock_speed, dual_sim, fc, 
        four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, 
        talk_time, three_g, touch_screen, wifi]]))

        return render_template('mobile_classify.html', mprediction="This is {}".format(mprediction)+" Phone")
    else:
        return render_template('mobile_classify.html')



if __name__ == '__main__':
    mobileclassifys.run(debug=True)
