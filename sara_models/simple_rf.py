import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_json('data/data.json')
df = pd.DataFrame(data)
df[‘fraud’] = [1 if x in [‘fraudster’,‘fraudster_event’,‘fraud_att’] else 0 for x in df['acct_type']]

y = df['acct_type']
X = df.drop('acct_type', axis=1)
X_lin=X.drop(df.columns['country','description','email_domain', 'listed','name','org_desc','org_name','payee_name','payout_type','previous_payouts','ticket_types','venue_address','venue_country','venue_name','venue_state'],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X_lin, y)

rf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=True, n_jobs=0, random_state=None)
rf = rf.fit(X_Train,y_train)
sco = rf.score(X_Train,y_train)
