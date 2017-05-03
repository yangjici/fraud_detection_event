import utils as u
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

# Run basic logistic regression
def run_model():

    print X_train.shape
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_predict)
    precision = precision_score(y_test, y_predict)
    recall = recall_score(y_test, y_predict)

    return accuracy, precision, recall

# Cross Validate linear regression
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

    #a, p, r = run_model(model, X_train, X_test, y_train, y_test)
    a, p, r = run_model()
    print a, p, r


def do_GridSearch(X_train,y_train):
    params = {
        'C': np.logspace(-4, 4, 30)
    }
    gs_model = GridSearchCV(model,params,n_jobs=-1)
    gs_model.fit(X_train,y_train)


def get_probabilities(X_test):

    return model.predict_proba(X_test)[:, 1]


def roc_curve(probabilities, labels):
    '''
    INPUT: numpy array, numpy array
    OUTPUT: list, list, list

    Take a numpy array of the predicted probabilities and a numpy array of the
    true labels.
    Return the True Positive Rates, False Positive Rates and Thresholds for the
    ROC curve.
    '''

    thresholds = np.sort(probabilities)

    tprs = []
    fprs = []

    num_positive_cases = sum(labels)
    num_negative_cases = len(labels) - num_positive_cases

    for threshold in thresholds:
        # With this threshold, give the prediction of each instance
        predicted_positive = probabilities >= threshold
        # Calculate the number of correctly predicted positive cases
        true_positives = np.sum(predicted_positive * labels)
        # Calculate the number of incorrectly predicted positive cases
        false_positives = np.sum(predicted_positive) - true_positives
        # Calculate the True Positive Rate
        tpr = true_positives / float(num_positive_cases)
        # Calculate the False Positive Rate
        fpr = false_positives / float(num_negative_cases)

        fprs.append(fpr)
        tprs.append(tpr)

    return tprs, fprs, thresholds.tolist()


def plot_roc(X_test, y_test):

    tpr, fpr, thresholds = roc_curve(get_probabilities(X_test), y_test)
    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Sensitivity, Recall)")
    plt.title("ROC plot of admissions data")
    plt.show()

if __name__ == "__main__":

    df = u.get_df(path='../data/data.json')
    y = df.pop('fraud')
    X = df
    X_nums = u.get_numeric_cols(df)
    X_nums = u.impute_median(X_nums, X_nums.columns)
    #
    # df['fraud'] = [1 if x in ['fraudster', 'fraudster_event', 'fraud_att'] else 0 for x in df.acct_type]
    #
    model = LogisticRegression()
    X_train, X_test, y_train, y_test = train_test_split(X_nums, y)
    print df.shape
    # run_ticket_types(df)
