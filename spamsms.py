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

spamsmsc = Blueprint('spamsms', __name__)


@spamsmsc.route("/spamsms")
def restaurant():
    return render_template('spam_sms.html')


# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'spam-sms-mnb-model.sav'
model = pickle.load(open(filename, 'rb'))
spamcv = pickle.load(open('cvsms-transform.sav', 'rb'))


@spamsmsc.route('/smspredict', methods=['POST'])
def smspredict():
    if request.method == 'POST':
        smsmessage = request.form['smsmessage']
        data = [smsmessage]
        vect = spamcv.transform(data).toarray()
        sms_prediction = model.predict(vect)
        return render_template('spam_sms.html', smsprediction=sms_prediction)


if __name__ == '__main__':
    spamsmsc.run(debug=True)
