from flask import Flask, Blueprint, render_template, request, app, redirect, url_for
import pickle
import json
import numpy as np
import pandas as pd 
import sklearn
import nltk
from flask import Response
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler

carprices = Blueprint('carprice', __name__)

@carprices.route("/carprice")
def carprice():
    return render_template('car_price.html')

@carprices.route("/predict", methods=['POST'])
def predictRoute():
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

#car_price_sandardScalar.sav     car_price_liner_model.sav
def predict_log(dict_pred):
    with open("car_price_sandardScalar.sav", 'rb') as f:
        scalar = pickle.load(f)

    with open("car_price_liner_model.sav", 'rb') as f:
        model = pickle.load(f)

    data_df = pd.DataFrame(dict_pred, index=[1, ])
    scaled_data = scalar.transform(data_df)
    predict = model.predict(scaled_data)
    return predict


@carprices.route("/pridict", methods=['POST'])
def pridict():

    Alfa_Romero = 0
    Audi = 0
    BMW = 0
    Chevrolet_Impala = 0
    Dodge_Rampage = 0
    Honda = 0
    Isuzu = 0
    Jaguar = 0
    Maxda = 0
    Buick_Electra = 0
    Mercury_Cougar = 0
    Mitsubishi = 0
    Nissan = 0
    Peugeot = 0
    Plymouth = 0
    Porsche_Macan = 0
    Renault = 0
    Saab = 0
    Subaru = 0
    Toyota = 0
    Vokswagen = 0
    VW_Dasher = 0
    Volkswagen = 0
    Gas = 0
    Diesel = 0
    Standard = 0
    Turbo = 0
    Two = 0
    Four = 0
    Forward = 0
    Reverseward = 0
    Front = 0
    Rear = 0
    Conver_Tible = 0
    Hatch_Back = 0
    Sedan = 0
    Wagon = 0
    Hard_Top = 0
    dohc = 0
    ohcv = 0
    ohc = 0
    rotor = 0
    ohcf = 0
    dohcv = 0
    Two = 0
    Three = 0
    Four = 0
    Five = 0
    Six = 0
    Eight = 0
    Twelve = 0
    mpfi = 0
    bbl = 0
    mfi = 0
    spfi = 0
    idi = 0
    spdi = 0

    if request.method == "POST":
        CarName_N = str(request.form['CarName_N'])
        symboling = int(request.form['symboling'])
        fueltype = request.form['fueltype']
        aspiration = request.form['aspiration']
        doornumber = request.form['doornumber']
        carbody = int(request.form['carbody'])
        drivewheel = request.form['drivewheel']
        enginelocation = request.form['enginelocation']
        wheelbase = float(request.form['wheelbase'])
        carlength = float(request.form['carlength'])
        carwidth = float(request.form['carwidth'])
        carheight = float(request.form['carheight'])
        curbweight = int(request.form['curbweight'])
        enginetype = int(request.form['enginetype'])
        cylindernumber = int(request.form['cylindernumber'])
        enginesize = int(request.form['enginesize'])
        fuelsystem = int(request.form['fuelsystem'])
        boreratio = float(request.form['boreratio'])
        stroke = float(request.form['stroke'])
        compressionratio = float(request.form['compressionratio'])
        horsepower = int(request.form['horsepower'])
        peakrpm = int(request.form['peakrpm'])
        citympg = int(request.form['citympg'])
        highwaympg = int(request.form['highwaympg'])


        if CarName_N == "Alfa_Romero":
            Alfa_Romero=0
        elif CarName_N == "Audi":
            Audi=1
        elif CarName_N == "BMW":
            BMW=2
        elif CarName_N == "Chevrolet_Impala":
            Chevrolet_Impala=3
        elif CarName_N == "Dodge_Rampage":
            Dodge_Rampage=4
        elif CarName_N == "Honda":
            Honda=5
        elif CarName_N == "Isuzu":
            Isuzu=6
        elif CarName_N == "Jaguar":
            Jaguar=7
        elif CarName_N == "Maxda":
            Maxda=8
        elif CarName_N == "Buick_Electra":
            Buick_Electra=9
        elif CarName_N == "Mercury_Cougar":
            Mercury_Cougar=10
        elif CarName_N == "Mitsubishi":
            Mitsubishi=11
        elif CarName_N == "Nissan":
            Nissan=12
        elif CarName_N == "Peugeot":
            Peugeot=13
        elif CarName_N == "Plymouth":
            Plymouth=14
        elif CarName_N == "Porsche_Macan":
            Porsche_Macan=15
        elif CarName_N == "Renault":
            Renault=16
        elif CarName_N == "Saab":
            Saab=17
        elif CarName_N == "Subaru":
            Subaru=18
        elif CarName_N == "Toyota":
            Toyota=19
        elif CarName_N == "Vokswagen":
            Vokswagen=20
        elif CarName_N == "VW_Dasher":
            VW_Dasher=21
        else:
            Volkswagen=22

        if fueltype == "Gas":
            Gas = 0
        else:
            Diesel = 1

        if aspiration == "Standard":
            Standard = 0
        else:
            Turbo = 1

        if doornumber == "Two":
            Two = 0
        else:
            Four = 1

        if drivewheel == "Forward":
            Forward = 1
        elif drivewheel == "Reverseward":
            Reverseward = 0

        if enginelocation == "Front":
            Front = 0
        else:
            Rear = 1
        
        if carbody == "Conver_Tible":
            Conver_Tible = 0
        elif carbody == "Hatch_Back":
            Hatch_Back = 1
        elif carbody == "Sedan":
            Sedan = 2
        elif carbody == "Wagon":
            Wagon = 3
        else:
            Hard_Top = 4

        if enginetype == "dohc":
            dohc = 0
        elif enginetype == "ohcv":
            ohcv = 1
        elif enginetype == "ohc":
            ohc = 2
        elif enginetype == "rotor":
            rotor = 4
        elif enginetype == "ohcf":
            ohcf = 5
        else:
            dohcv = 6

        if cylindernumber == "Two":
            Two = 0
        elif cylindernumber == "Three":
            Three = 1
        elif cylindernumber == "Four":
            Four = 2
        elif cylindernumber == "Five":
            Five = 3
        elif cylindernumber == "Six":
            Six = 4
        elif cylindernumber == "Eight":
            Eight = 5
        else:
            Twelve = 6


        if fuelsystem == "mpfi":
            mpfi = 0
        elif fuelsystem == "bbl":
            bbl = 1
        elif fuelsystem == "mfi":
            mfi = 2
        elif fuelsystem == "spfi":
            spfi = 3
        elif fuelsystem == "idi":
            idi = 4
        else:
            spdi = 5


        prediction = predict_log(np.array([[CarName_N, symboling, fueltype, aspiration, doornumber, carbody, drivewheel, 
        enginelocation, wheelbase, carlength, carwidth, carheight, curbweight, enginetype, cylindernumber, enginesize, 
        fuelsystem, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]]))
        
        
        output = round(prediction[0])

        return render_template('car_price.html', prediction="Your Estimated Car Price is {}".format(output)+" Tk.")
    else:
        return render_template('car_price.html')


if __name__ == '__main__':
    carprices.run(debug=True)
