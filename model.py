import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import datetime
from data_cleaning import *


df = pd.read_json('data/data.json')

fraud_flags = ['fraudster_event', 'fraudster', 'fraudster_att']


df['Fraud'] = df['acct_type'].map(lambda x: 1 if x in fraud_flags else 0) # creating boolean values for Fraud response variable

df.drop('acct_type', axis = 1, inplace=True) # Remove 'acct_type' column to avoid leakage


'''
Feature Engineering
'''
######
# previous_payouts
#
def make_time(t):
    return datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

def payout_info(row):
    no_payout=np.array([0,0]).reshape(1,2)
    if (row!=[]):
        if 'created' in row[0]:
            time_list =list(set([pay['created'] for pay in row]))
            time_object = sorted([make_time(t) for t in time_list])
            time_int = [time_object[n]-time_object[n-1] for n in range(1,len(time_object))]
            days_int = np.array([dt.days for dt in time_int])
            median_day = np.median(days_int)
            return np.array([1,median_day]).reshape(1,2)
    else:
        return no_payout


payout_features = np.array([0,0]).reshape(1,2)

for i in df.previous_payouts:
    payout = payout_info(i)
    payout_features = np.append(payout,payout_features,axis=0)

payout_features = pd.DataFrame(payout_features[1:,],columns=['number_payout','median_day_interval'])

df = pd.concat([df,payout_features],axis=1)

############
def make_price(row):
    s2=np.array([0,0,0]).reshape(1,3)
    if (row!= []):
        if ('cost' in row[0]):
            prices=[int(tic['cost']) for tic in row]
            s1 = np.array([len(row),min(prices),max(prices)]).reshape(1,3)
            return s1
    else:
        return s2

price_features = np.array([0,0,0]).reshape(1,3)

for i in df.ticket_types:
    price = make_price(i)
    price_features = np.append(price_features,price,axis=0)


price_features = pd.DataFrame(price_features[1:,],columns=['number_tickets','min_price','max_price'])

df = pd.concat([df,price_features],axis=1)

############

categorical_features = ['currency', 'listed', 'payout_type']

features_to_engineer = ['country', 'description', 'email_domain', 'name', 'org_desc', 'org_name', 'payee_name', 'previous_payouts', 'ticket_types', 'venue_address', 'venue_name', 'venue_country' ,'venue_state', 'sale_duration2', 'sale_duration','number_payout']

for feature in categorical_features:
    df = dummify(df,feature)

X = df.copy()
for feature in features_to_engineer:
    X = X.drop(feature, axis = 1)

X = remove_missing_values(X, 'venue_latitude')

X = add_zeros(X, 'has_header')

# columns_to_keep = []

y = X['Fraud']

X = X.drop('Fraud', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 100)

# Creating cross-validated datasets
X_train_CV, X_test_CV, y_train_CV, y_test_CV = train_test_split(X_train, y_train)


# Fitting Random Forest model into our cross-validated data
rf = RandomForestClassifier()
rf = rf.fit(X_train_CV, y_train_CV)

# Making predictions

predictions_rf = rf.predict(X_test_CV)
accuracy_rf = sum(predictions_rf==y_test_CV)/float(len(y_test_CV))
precision_rf = sum((predictions_rf==1) & (predictions_rf==y_test_CV)) /float(sum(predictions_rf==1))
recall_rf = sum((predictions_rf==1) & (predictions_rf==y_test_CV))/float(sum(y_test_CV==1))

print 'Random Forests results: ', accuracy_rf, precision_rf, recall_rf

# Fitting Adaboost model into our cross-validated data
ada = AdaBoostClassifier()
ada = ada.fit(X_train_CV, y_train_CV)

# Making predictions

predictions_ada = ada.predict(X_test_CV)
accuracy_ada = sum(predictions_ada==y_test_CV)/float(len(y_test_CV))
precision_ada = sum((predictions_ada==1) & (predictions_ada==y_test_CV)) /float(sum(predictions_ada==1))
recall_ada = sum((predictions_ada==1) & (predictions_ada==y_test_CV))/float(sum(y_test_CV==1))

print 'Adaboost results: ', accuracy_ada, precision_ada, recall_ada
