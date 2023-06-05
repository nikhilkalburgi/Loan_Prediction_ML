from flask import Flask,render_template,url_for,request
import seaborn as sns
import matplotlib
import os
from datetime import datetime
import json
import numpy as np
import pandas as pd
matplotlib.use('Agg')
result = None
model = None
from logisticRegression import LogisticReg
from svm import SVM
from knn import KNN
from sgd import SGD
from gbc import GBC
from gbr import GBR
from DecisionTree import DT
from RandomForest import RFC
from xgb import XGB
from Naive_Bayes import Naive
from ANN import  Artificial_N_N
# Data Preprocessing
from processing import processMyFile,getDf

def initiate_app():

    return render_template('index.html', name="hello")

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
def hello_world():
    return initiate_app()

@app.post("/filepath")
def url(): 
    return processMyFile(request.get_json())

@app.post("/plot")
def plot():
    try:
        date= datetime.utcnow() - datetime(1970, 1, 1)
        seconds =(date.total_seconds())
        num = str(round(seconds*1000))
        res = request.get_json() 
        if  res['type'] == 'Scatter Plot':
            df = getDf()
            plot = sns.scatterplot(x=res['x'].strip(),y=res['y'].strip(),hue=res['hue'].strip(),data=df)
            matplotlib.pyplot.savefig('static/plot'+num+'.png')
        elif  res['type'] == 'Bar Plot':   
            df = getDf()
            plot = sns.barplot(x=res['x'].strip(),y=res['y'].strip(),hue=res['hue'].strip(),data=df)
            matplotlib.pyplot.savefig('static/plot'+num+'.png')
        elif  res['type'] == 'Pair Plot':   
            df = getDf()
            plot = sns.pairplot(df,hue='Loan_Status')
            matplotlib.pyplot.savefig('static/plot'+num+'.png')
        elif  res['type'] == 'Count Plot':   
            df = getDf()
            plot = sns.countplot(df,x=res['y'].strip(),hue=res['hue'].strip())
            matplotlib.pyplot.savefig('static/plot'+num+'.png')
        elif  res['type'] == 'Heat Map':   
            df = getDf()
            plot = sns.heatmap(df[['ApplicantIncome'	,'CoapplicantIncome',	'LoanAmount'	,'Loan_Amount_Term'	,'Credit_History']].corr());
            matplotlib.pyplot.savefig('static/plot'+num+'.png') 
        matplotlib.pyplot.clf()                   
        return '<img src="static/plot'+num+'.png" style="object-fit:contain;" width="100%" height="100%">'  
    except:
        return "0"
    
@app.post("/model")
def model():
    res = request.get_json() 
    global result
    global model
    print(res)
    try:
        if res == "Logistic Regression":
            # Logistic Regression
            result = LogisticReg()

        if res == "Support Vector Classifier":    
            # Support Vector Machine (SVM)
            result = SVM()
        
        if res == "K-Nearest Neighbour":            

            # K - Nearest Neighbour (KNN)
            result = KNN()

        if res == "Shochastic Gradient Descent": 
            # Stochastic Gradient Descent
            result = SGD()

        if res == "GradientBoostingClassifier":
            # GradientBoostingClassifier
            result = GBC()

        if res == "GradientBoostingRegressor":
            # GradientBoostingRegressor
            result = GBR()

        if res == "Decision Tree":
            #DecisionTree
            result = DT()

        if res == "Random Forest":
            #RandomForest Classifier
            result = RFC()

        if res == "XGBoost":
            #XGBoost

            result = XGB()

        if res == "Naive Bayes":
            # Naive Bayes
            result=Naive()

        if res == "Artificial Neural Network":
            # Artificial Neural Networks
            result=Artificial_N_N()

    except:
        return "0" 
    model = result.pop('model') 
    return json.dumps(result)    

@app.post("/pp")
def pp():
    try:

        res = request.get_json()
        res = res.replace("Male","1")
        res = res.replace("Female","0")
        res = res.replace("Yes","1")
        res = res.replace("No","0")
        res = res.replace("3+","3")
        res = res.replace("Urban","2")
        res = res.replace("Rural","0")
        res = res.replace("Semiurban","1")
        res = res.replace("Not Graduate","0")
        res = res.replace("Graduate","1")
        res = res.replace("0t 1","0")
        res = res.split(",")
        print(res)
        res = [int(i) for i in res]
        return str(model.predict(pd.DataFrame([res],columns=['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])))
    except :
        return "0"

app.run()   



