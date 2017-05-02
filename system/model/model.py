from sklearn.ensemble import RandomForestClassifier

class Model(object):
    def __init__(self):
        pass

    def fit(self, X, y):
        r = RandomForestClassifier()
        return r.fit(X, y)

    def predict(self, X):
        pass
