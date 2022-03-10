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

moviegenrem = Blueprint('moviegenre', __name__)

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'movie-genre-mnb-model.sav'
mov_classifier = pickle.load(open(filename, 'rb'))
movcv = pickle.load(open('movcv-transform.sav', 'rb'))

@moviegenrem.route("/moviegenre")
def moviegenre():
    return render_template('movies_genre.html')

@moviegenrem.route('/movpredict', methods=['POST'])
def movpredict():
    if request.method == 'POST':
        movscript = request.form['movscript']
        movdata = [movscript]
        movvect = movcv.transform(movdata).toarray()
        mov_prediction = mov_classifier.predict(movvect)
        return render_template('movies_genre.html', movprediction=mov_prediction)


if __name__ == '__main__':
    moviegenrem.run(debug=True)