import pandas as pd
import numpy as np
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score,f1_score

train_df = pd.read_csv("data/loanData.csv")

train_df.dropna(inplace = True)
train_df = train_df.drop(columns=['Loan_ID'])

train_df = pd.get_dummies(train_df,drop_first=True)

print(train_df.info())
X = train_df.drop(columns=["Loan_Status_Y"])
y = train_df["Loan_Status_Y"].values.reshape(-1,1)

X.dropna(inplace = True)



tree_clf = DecisionTreeClassifier()
tree_clf.fit(X,y)

test = pd.read_csv("data/testData.csv")

test.dropna(inplace = True)
op = test.copy()
test = test.drop(columns=['Loan_ID'])

test = pd.get_dummies(test,drop_first=True)


y_pred = tree_clf.predict(test)


op['Loan_Status'] = y_pred

op = op.apply(lambda x: x.replace({True:'Y', False:'N'}, regex=True))

op.to_csv('data/Loan_Data.csv')