import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import json

data = dict()
df = None
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

def processMyFile(file):

    global data
    global df
    try :

        df = pd.read_csv(file)
        res = {"prevshape":df.shape}
        df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
        df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].median())
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
        df['ApplicantIncome'] = df['ApplicantIncome'].fillna(df['ApplicantIncome'].mean())
        df['CoapplicantIncome'] = df['CoapplicantIncome'].fillna(df['CoapplicantIncome'].mean())
        df.dropna(inplace = True)
        df = df.drop(columns=["Loan_ID"])
        df = df.loc[~df.duplicated()].reset_index(drop=True).copy()
        numeric_df = df.copy()
        numeric_df['Loan_Status'].replace('Y',1,inplace=True)
        numeric_df['Loan_Status'].replace('N',0,inplace=True)
        numeric_df.Gender=numeric_df.Gender.map({'Male':1,'Female':0})
        numeric_df.Married=numeric_df.Married.map({'Yes':1,'No':0})
        numeric_df.Dependents=numeric_df.Dependents.map({'0':0,'1':1,'2':2,'3+':3})
        numeric_df.Education=numeric_df.Education.map({'Graduate':1,'Not Graduate':0})
        numeric_df.Self_Employed=numeric_df.Self_Employed.map({'Yes':1,'No':0})
        numeric_df.Property_Area=numeric_df.Property_Area.map({'Urban':2,'Rural':0,'Semiurban':1})


        data['X']= numeric_df.drop(columns=["Loan_Status"])
        data['y'] = numeric_df["Loan_Status"].values.reshape(-1,1)
        data['X_train'], data['X_test'], data['y_train'], data['y_test'] = train_test_split(data['X'],data['y'],test_size=0.3,random_state=42)
    except :
        return "0"
    res["head"]= numeric_df.head().to_html(escape=False, formatters=dict(Country=path_to_image_html))
    res["shape"]= numeric_df.shape
    
    return json.dumps(res)

        
def getDf():
    return df
