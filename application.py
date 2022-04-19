from flask import Flask, render_template, request
import joblib
from joblib import load
import numpy as np

# load the saved pipleine model
model = load("xgbcarpricepredictor.joblib")

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data1 = int(data1)
    data2 = request.form['b']
    data2 = int(data2)
    data3 = request.form['c']
    data3 = int(data3)
    data4 = request.form['d']
    data4 = int(data4)
    data5 = request.form['e']
    data5 = int(data5)
    data6 = request.form['f']
    data6 = int(data6)
    data7 = request.form['g']
    data7 = int(data7)
    data8 = request.form['h']
    data8 = int(data8)
    data9 = request.form['i']
    data9 = int(data9)
    data10 = request.form['j']
    data10 = int(data10)
    data11 = request.form['k']
    data11 = int(data11)
    data12 = request.form['l']
    data12 = int(data12)
    data13 = request.form['m']
    data13 = int(data13)
    data14 = request.form['n']
    data14 = int(data14)
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)