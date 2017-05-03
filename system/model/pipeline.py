import re
import pandas as pd
import numpy as np
import cPickle as pickle
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from model import Model

class Pipeline(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def get_X_y(self):
        df = pd.read_json(self.filepath)
        bool_mask = (df['acct_type'] == 'premium') | (df['acct_type'].apply(lambda x: re.match('fraud', x)))
        df = df[bool_mask]
        df['fraud'] = df['acct_type'].apply(lambda x: re.match('fraud', x) != None)
        df['text'] = df['description'].apply(lambda html: BeautifulSoup(html, "html5lib").text)
        df.pop('acct_type')
        df.pop('description')
        v = TfidfVectorizer(stop_words='english',max_features=300)
        X = v.fit_transform(df.text).toarray()
        y = df.fraud.values
        return X, y

    def train(self, X, y):
        return Model().fit(X, y)

    def save_model(self, model, filepath):
        with open(filepath, 'w') as f:
            pickle.dump(model, f)
