from sklearn.linear_model import LogisticRegression

from processing import data
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def LogisticReg():
    obj = dict()
    logReg = LogisticRegression(max_iter=1000)
    logReg.fit(data['X_train'],data['y_train'].ravel())

    y_pred = logReg.predict(data['X_test'])

    obj["model"] = logReg

    obj["score"] = logReg.score(data['X_train'],data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred, zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred,data['y_test'])

    return obj
