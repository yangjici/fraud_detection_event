import re
import pandas as pd
import numpy as np
import cPickle as pickle
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from model import Model
from feature_eng import *

class Pipeline(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.model = None

    def get_X_y(self):
        df = pd.read_json(self.filepath)

        df['fraud'] = [1 if x in ['fraudster','fraudster_event','fraud_att'] else 0 for x in df.acct_type]

        df['has_description'] = [1 if x!='' else 0 for x in df['org_desc'] ]
        df['has_org_name'] = [1 if x!='' else 0 for x in df['org_name'] ]
        df['has_address']=[1 if x!='' else 0 for x in df['venue_address']]
        df['has_payout']= [1 if x != '' else 0 for x in df['payout_type']]

        #add price and ticket info
        df=add_price(df)
        #add previous_payouts and time interval
        df=make_payout(df)


        features_to_include = ['gts','has_description','has_org_name','has_address','user_age','user_type','ticket_num','has_payout','max_price','min_price','number_previous_payout']
        X=df[features_to_include]

        y = df.fraud.values
        return X, y

    def processor(self, datapoint):
        df = pd.read_json(datapoint)
        # df['text'] = df['description'].apply(lambda html: BeautifulSoup(html, "html5lib").text)
        df['has_description'] = [1 if x!='' else 0 for x in df['org_desc'] ]
        df['has_org_name'] = [1 if x!='' else 0 for x in df['org_name'] ]
        df['has_address']=[1 if x!='' else 0 for x in df['venue_address']]
        df['has_payout']= [1 if x != '' else 0 for x in df['payout_type']]

        #add price and ticket info
        df=add_price(df)
        #add previous_payouts and time interval
        df=make_payout(df)


        features_to_include = ['gts','has_description','has_org_name','has_address','user_age','user_type','ticket_num','has_payout','max_price','min_price','number_previous_payout']

        X=df[features_to_include]

        return X

    def train(self, X, y):
        self.model = Model()
        self.model.fit(X, y)
        return self.model

    def save_model(self, model, filepath):
        with open(filepath, 'w') as f:
            pickle.dump(model, f)

    def predict(self,X):
        return self.model.predict(X)
