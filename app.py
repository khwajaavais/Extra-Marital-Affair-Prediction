from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('logistic_reg.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        INTERCEPT = 1
        RATE_MARRIAGE = request.form['Rate_Marriage']
        Years_Married = request.form['Years_Married']        
        Children = request.form['Children']
        Women_Age = request.form['Women_Age']
        Religious = request.form['Religious']
        Education = request.form['Education']
        W_Occ = request.form['W_Occ']
        if W_Occ == 2 :
            w_occ_2 = 1
            w_occ_3,w_occ_4,w_occ_5,w_occ_6 = 0,0,0,0
        elif W_Occ == 3:
            w_occ_3 = 1
            w_occ_2,w_occ_4,w_occ_5,w_occ_6 = 0,0,0,0
        elif W_Occ == 4:
            w_occ_4 = 1
            w_occ_2,w_occ_3,w_occ_5,w_occ_6 = 0,0,0,0
        elif W_Occ == 5:
            w_occ_5 = 1
            w_occ_2,w_occ_4,w_occ_3,w_occ_6 = 0,0,0,0
        else:
            w_occ_6 = 1
            w_occ_2,w_occ_4,w_occ_5,w_occ_3 = 0,0,0,0
            
            
        H_Occ = request.form['H_Occ']
        if H_Occ == 2 :
            h_occ_2 = 1
            h_occ_3,h_occ_4,h_occ_5,h_occ_6 = 0,0,0,0
        elif H_Occ == 3:
            h_occ_3 = 1
            h_occ_2,h_occ_4,h_occ_5,h_occ_6 = 0,0,0,0
        elif H_Occ == 4:
            h_occ_4 = 1
            h_occ_2,h_occ_3,h_occ_5,h_occ_6 = 0,0,0,0
        elif H_Occ == 5:
            h_occ_5 = 1
            h_occ_2,h_occ_4,h_occ_3,h_occ_6 = 0,0,0,0
        else:
            h_occ_6 = 1
            h_occ_2,h_occ_4,h_occ_5,h_occ_3 = 0,0,0,0

        try:    
            prediction = model.predict([[ INTERCEPT, w_occ_2, w_occ_3, w_occ_4, w_occ_5, w_occ_6,
                                           h_occ_2,h_occ_3,h_occ_4,h_occ_5,h_occ_6, RATE_MARRIAGE, Women_Age, Years_Married, Children, Religious, Education]])
        
            
            if prediction[0] == 0:
                return render_template('result.html',prediction_text="HURRAY!!!!!!!! NO MARITAL AFFAIR 😃")
            else:
                return render_template('result.html',prediction_text="OOOPS!!!!!!!! MARITAL AFFAIR FOUND 😟 😮")
            
            print(prediction[0])
            
        except:
            return render_template('index.html')
        
        
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

