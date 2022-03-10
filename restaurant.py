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

restaurantr = Blueprint('restaurant', __name__)


@restaurantr.route("/restaurant")
def restaurant():
    return render_template('restaurant_reviews.html')


# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'restaurantr-sentiment-mnb-model.sav'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transformres.sav', 'rb'))


@restaurantr.route('/respredict', methods=['POST'])
def respridict():
    if request.method == 'POST':
        review = request.form['review']
        data = [review]
        vect = cv.transform(data).toarray()
        res_prediction = classifier.predict(vect)
        return render_template('restaurant_reviews.html', resprediction=res_prediction)


if __name__ == '__main__':
    restaurantr.run(debug=True)
