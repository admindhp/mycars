from flask import Flask,request,jsonify
import pandas as pd
from flask_cors import cross_origin
import numpy

app = Flask(__name__)


@app.route('/',methods=["GET"])
@cross_origin(origins="*")
def data():
    cars = pd.read_csv('Cleaned_Car_data.csv')
    cars = cars.to_numpy()
    cars_list = []
    for car in cars:
        c={}
        c['Model'] = car[1]
        c['Company'] = car[2]
        c['Year'] = car[3]
        c['Price'] = car[4]
        c['Kilometer_Driven'] = car[5]
        c['Fuel_Type'] = car[6]
        c['Image']=car[7]
        c['Seats']=car[8]
        c['Logo']=car[9]
        cars_list.append(c)
    return jsonify(cars_list)

if __name__ == "__main__":
    app.run(debug=True)
