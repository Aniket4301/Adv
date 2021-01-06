from flask import Flask, render_template, request
import pickle
import jsonify
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('new1122.pickle', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('input.html')

standard_to = StandardScaler()
@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        newspaper = float(request.form['newspaper'])
        radio = float(request.form['radio'])
        TV = float(request.form['TV'])

        prediction = model.predict([[newspaper, radio, TV]])
        return render_template('home.html', prediction_text="Sale is {}".format(prediction))
    else:
        return render_template('input.html')


if __name__ == "__main__":
    app.run(debug=True)
