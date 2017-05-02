import utils as u
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score


model = LogisticRegression()


def init():
    try:
        df
    except NameError:
        df = u.get_df(path='../data/data.json')

# Run basic logistic regression
def run_model(model, X_train, X_test, y_train, y_test):

    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_predict)
    precision = precision_score(y_test, y_predict)
    recall = recall_score(y_test, y_predict)

    return accuracy, precision, recall


def run_model_cv(model, X_train, X_test, y_train, y_test):

    kfold = KFold(n_splits=5)

    accuracies = []
    precisions = []
    recalls = []

    for train_index, test_index in kfold:

        model.fit(X[train_index], y[train_index])
        y_predict = model.predict(X[test_index])
        y_true = y[test_index]

        accuracies.append(accuracy_score(y_true, y_predict))
        precisions.append(precision_score(y_true, y_predict))
        recalls.append(recall_score(y_true, y_predict))

    accuracies_avg = np.average(accuracies)
    precisions_avg = np.average(precisions)
    recalls_avg = np.average(recalls)

    # print "accuracy:", np.average(accuracies)
    # print "precision:", np.average(precisions)
    # print "recall:", np.average(recalls)

    return accuracies_avg, precisions_avg, recalls_avg


def run_ticket_types(in_df):
    df = in_df.copy()
    tix_df = u.get_ticket_types_df(df)
    y = tix_df.pop('fraud')
    X = tix_df
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    a, p, r = run_model(model, X_train, X_test, y_train, y_test)
    print a, p, r
