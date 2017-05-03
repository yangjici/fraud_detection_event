from sklearn.ensemble import RandomForestClassifier

class Model(object):
    def __init__(self):
        self.model =None


    def fit(self, X, y):
        self.model = RandomForestClassifier(n_estimators=1000, class_weight='balanced',
                                   max_features='auto', min_samples_split=10 )
        self.model.fit(X,y)

        return self.model

    def predict(self, X):
        predictions = self.model.predict(X)
        probability = self.model.predict_proba(X)[0][1]
        return predictions, probability
