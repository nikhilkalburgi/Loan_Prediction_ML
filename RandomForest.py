from sklearn.ensemble import RandomForestClassifier 

from processing import data
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def RFC():
    obj = dict()
    rfc = RandomForestClassifier(n_estimators=100,max_depth=3,min_samples_leaf = 10)
    rfc.fit(data['X_train'], data['y_train'].ravel())

    y_pred = rfc.predict(data['X_test'])

    obj["model"] = rfc

    obj["score"] = rfc.score(data['X_train'], data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred.round(), zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred.round(), data['y_test'])

    return obj