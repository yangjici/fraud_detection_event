import cPickle as pickle
from flask import Flask, request, jsonify
import pandas as pd
import pymongo, json
import argparse



'''Creates flask app backbone.
'''

app = Flask(__name__)
@app.route('/')

def predict(data):
    """Recieve the data from input form and use model to predict.
    """
    pred = model.predict(data)
    proba = model.predict_proba(data)
    return jsonify((pred,proba),data)

#will have data pushed to

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='.')
    parser.add_argument('--data', help='The input data')
    parser.add_argument('--out', help='A file to save the pickled model object to.')
    args = parser.parse_args()

    X, y = get_data(args.data)
    m = model()
    app.run(host='0.0.0.0', debug=True)
    with open(args.out, 'w') as f:
        pickle.dump(m, f)
    with open('model/pipeline.pkl') as f:
        model = pickle.load(f)
