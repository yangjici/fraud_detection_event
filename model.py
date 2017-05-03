import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from data_cleaning import *


df = pd.read_json('data.json')

fraud_flags = ['fraudster_event', 'fraudster', 'fraudster_att']


df['Fraud'] = df['acct_type'].map(lambda x: 1 if x in fraud_flags else 0) # creating boolean values for Fraud response variable

df.drop('acct_type', axis = 1, inplace=True) # Remove 'acct_type' column to avoid leakage

categorical_features = ['currency', 'listed', 'payout_type']

features_to_engineer = ['country', 'description', 'email_domain', 'name', 'org_desc', 'org_name', 'payee_name', 'previous_payouts', 'ticket_types', 'venue_address', 'venue_name', 'venue_country' ,'venue_state']

'''
Feature Engineering
'''
######
# previous_payouts

def make_time(t):
    return datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

def payout_info(row):
    no_payout=np.array([0,None]).reshape(1,2)
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

df_price_payout = pd.concat([df_price,payout_features],axis=1)

############

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
accuracy_rf = sum(predictions==y_test_CV)/float(len(y_test_CV))
precision_rf = sum((predictions==1) & (predictions==y_test_CV)) /float(sum(predictions==1))
recall = sum((predictions==1) & (predictions==y_test_CV))/float(sum(y_test_CV==1))

print 'Random Forests results: ' accuracy, precision, recall
