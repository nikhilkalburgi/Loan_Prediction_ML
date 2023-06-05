from sklearn.svm import SVC
from processing import data

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


def SVM():
    obj = dict()
    svm = SVC()

    svm.fit(data['X_train'],data['y_train'].ravel())
    y_pred = svm.predict(data['X_test'])

    obj["model"] = svm
    obj["score"] = svm.score(data['X_train'],data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred, zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred,data['y_test'])


    return obj