from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from processing import data
import numpy as np

# from processing import data


def Artificial_N_N():
    
    obj = dict()
    
    ANN_model = Sequential()

    ANN_model.add(Dense(12, input_dim=data['X'].shape[1], activation="relu"))

    ANN_model.add(Dense(8, activation="relu"))

    ANN_model.add(Dense(1, activation="sigmoid"))

    ANN_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    x = np.asarray(data['X_train']).astype('float32')
    y = np.asarray(data['y_train']).astype('float32')
    ANN_model.fit(x, y, epochs=100, batch_size=64)

    y_pred_proba = ANN_model.predict(np.asarray(data['X_test']).astype('float32'))
    y_pred = (y_pred_proba > 0.5).astype(int)

    obj["model"] = ANN_model


    obj["score"] = ANN_model.evaluate(x,y)
    obj["classification_report"] = classification_report(data['y_test'], y_pred, zero_division=0)
    obj["accuracy_score"] = accuracy_score(y_pred,data['y_test'])

    return obj


# Artificial_N_N()