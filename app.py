import pickle
from flask import Flask, request, jsonify,app,render_template
import numpy as np
import pandas as pd


app=Flask(__name__)
## load the model
regmodel=pickle.load(open('regmodel.pkl','rb')) 
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html') #pointing to home.html file in templates folder

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data1=request.json['data'] ##the data is in the form of json stored in data variable
    print(data1)
    new_data=scalar.transform(np.array(list(data1.values())).reshape(1,-1)) ##reshaping the data bcoz we are predicting for only one instance
    output=regmodel.predict(new_data) ##output will be predicted using the model
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]  ##getting the data from the form
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)    
    print(output[0])
    return render_template('home.html',prediction_text="The predicted house price is Rs. {:.2f}".format(output[0]))

if __name__=="__main__":
    app.run(debug=True)