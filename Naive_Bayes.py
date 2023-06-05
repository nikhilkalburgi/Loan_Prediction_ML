from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import classification_report

from processing import data

def Naive():
    
    obj = dict()

    nb = GaussianNB()

    nb.fit(data['X_train'],data['y_train'].ravel())

    y_pred = nb.predict(data['X_test'])

    obj["model"] = nb

    obj["score"] = nb.score(data['X_train'],data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred, zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred,data['y_test'])

    return obj


