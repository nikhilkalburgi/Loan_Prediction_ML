from sklearn.neighbors import KNeighborsClassifier

from processing import data
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def KNN():
    obj = dict()
    knn = KNeighborsClassifier()

    knn.fit(data['X_train'],data['y_train'].ravel())
    y_pred = knn.predict(data['X_test'])

    obj["model"] = knn
    obj["score"] = knn.score(data['X_train'],data['y_train'])
    obj["classification_report"] = classification_report(data['y_test'], y_pred, zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred,data['y_test'])

    return obj