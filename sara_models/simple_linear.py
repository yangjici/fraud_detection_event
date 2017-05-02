import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

#y = acct_type
data = pd.read_json('data/data.json')
df = pd.DataFrame(data)
#df[‘fraud’] = [1 if x in [‘fraudster’,‘fraudster_event’,‘fraud_att’] else 0 for x in df['acct_type']]

#folded = KFold(n_splits=3, shuffle=False, random_state=None)

y = df['acct_type']
X = df.drop('acct_type', axis=1)
X_lin=X.drop(df.columns['country','description','email_domain', 'listed','name','org_desc','org_name','payee_name','payout_type','previous_payouts','ticket_types','venue_address','venue_country','venue_name','venue_state'],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X_lin, y)

lm = LinearRegression()
lm = lm.fit(X_train, y_train)
sc = lm.score(X_train,y_train)

#pipeline portion:
#lm.predict
