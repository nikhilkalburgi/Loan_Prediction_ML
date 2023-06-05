from sklearn.linear_model import SGDClassifier

from processing import data
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def SGD():
    obj = dict()
    sgd = SGDClassifier(loss="hinge", penalty="l2", max_iter=40)
    sgd.fit(data['X_train'],data['y_train'].ravel())

    y_pred = sgd.predict(data['X_test'])

    obj["model"] = sgd

    obj["score"] = sgd.score(data['X_train'],data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred, zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred.round(),data['y_test'])

    return obj