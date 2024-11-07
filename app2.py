from flask import Flask, render_template, request
import pandas as pd
import numpy as np 
import pickle

app = Flask(__name__)
model = pickle.load(open("xgb_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)
    return render_template('index.html', prediction_text = "{}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)