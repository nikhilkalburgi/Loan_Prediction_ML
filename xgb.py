import xgboost as xgb

from processing import data
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def XGB():
    obj = dict()
    xg_b = xgb.XGBClassifier(n_estimators = 10)
    xg_b.fit(data['X_train'], data['y_train'].ravel())

    y_pred = xg_b.predict(data['X_test'])

    obj["model"] = xg_b

    obj["score"] = xg_b.score(data['X_train'], data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred.round(), zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred.round(), data['y_test'])

    return obj