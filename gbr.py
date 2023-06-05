from sklearn.ensemble import GradientBoostingRegressor

from processing import data
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def GBR():
    obj = dict()
    gbr = GradientBoostingRegressor()
    gbr.fit(data['X_train'],data['y_train'].ravel())

    y_pred = gbr.predict(data['X_test'])

    obj["model"] = gbr

    obj["score"] = gbr.score(data['X_train'],data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred.round(), zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred.round(),data['y_test'])

    return obj