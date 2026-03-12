from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form['age'])
    sex = float(request.form['sex'])
    tsh = float(request.form['tsh'])
    t3 = float(request.form['t3'])
    tt4 = float(request.form['tt4'])

    data = np.array([[age,sex,tsh,t3,tt4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Thyroid Positive"
    else:
        result = "Thyroid Negative"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)