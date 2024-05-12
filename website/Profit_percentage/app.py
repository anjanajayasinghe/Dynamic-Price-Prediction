from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# setup application
app = Flask(__name__,template_folder='template')

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict(lst)
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
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
        pred_value = prediction(m)
        pred_value = np.round(pred_value[0],2)
        pred_value
    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)

