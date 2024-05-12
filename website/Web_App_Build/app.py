from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

#Predictor Functions
def prediction1(lst1):
    with open('model/predictor1.pickle', 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict(lst1)
    return pred_value

def prediction2(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict(lst)
    return pred_value


#Main App Drawers
@app.route('/',methods=['POST','GET'])
def home():
    return render_template('index.html')


#2nd App Drawer
@app.route('/index1', methods=['POST', 'GET'])
def index1():
    pred_value = 0
    if request.method == 'POST':
        riders=request.form['riders']
        drivers=request.form['drivers']
        loyalty=request.form['loyalty']
        category=request.form['category']
        past_rides=request.form['past_rides']
        rating=request.form['rating']
        booking_time=request.form['booking_time']
        vehicle_type=request.form['vehicle_type']
        duration=request.form['duration']

        feature_list1 = []

        feature_list1.append(int(riders))
        feature_list1.append(int(drivers)) 
        feature_list1.append(category)
        feature_list1.append(loyalty)
        feature_list1.append(int(past_rides))
        feature_list1.append(float(rating))
        feature_list1.append(booking_time)
        feature_list1.append(vehicle_type)
        feature_list1.append(float(duration))

        print(feature_list1)
        m1=pd.DataFrame(columns=['Number_of_Riders', 'Number_of_Drivers','Location_Category','Customer_Loyalty_Status','Number_of_Past_Rides','Average_Ratings','Time_of_Booking','Vehicle_Type','Expected_Ride_Duration'])
        m1 = pd.concat([m1,pd.DataFrame([feature_list1],columns=['Number_of_Riders', 'Number_of_Drivers','Location_Category','Customer_Loyalty_Status','Number_of_Past_Rides','Average_Ratings','Time_of_Booking','Vehicle_Type','Expected_Ride_Duration'])], ignore_index=True)
        pred_value = prediction1(m1)
        pred_value = np.round(pred_value[0],2)
        pred_value
    return render_template('index1.html', pred_value=pred_value)

#2nd App Drawer
@app.route('/index2', methods=['POST', 'GET'])
def index2():
    pred_value = 0
    if request.method == 'POST':
        riders = request.form['riders']
        drivers = request.form['drivers']

        feature_list = []

        feature_list.append(riders)
        feature_list.append(drivers)
      
        print(feature_list)
        m=pd.DataFrame(columns=['Number_of_Riders', 'Number_of_Drivers'])
        m = pd.concat([m,pd.DataFrame([feature_list],columns=['Number_of_Riders', 'Number_of_Drivers'])], ignore_index=True)
        pred_value = prediction2(m)
        pred_value = np.round(pred_value[0],2)
        pred_value
    return render_template('index2.html', pred_value=pred_value)

if __name__=='__main__':
    app.run(debug=True)