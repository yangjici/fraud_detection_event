import requests
import time
from pymongo import MongoClient
import cPickle as pickle
import pandas as pd
import random
from feature_eng import *

client = MongoClient()
collection = client['fraud']['records']

#Pulls from url and returns json
def getjson():
    r = requests.get('https://galvanize-case-study-on-fraud.herokuapp.com/data_point')
    return r.json()

def add_record(json):
    """Adds record to MongoDB
    """
    json_id = collection.insert_one(json).inserted_id
    print "Inserted json at {}".format(json_id)

def pull_loop():
    """Infinite loop to pull json, run prediction, add to database, and check for duplicates.
    """
    current_object = 0
    while True:
        json = getjson()
        cur_obj_id = json["object_id"]
        if collection.find( { "object_id" : cur_obj_id } ).count() == 0:
            prediction, probability = predict(json)
            print "prediction {}, probability: {}".format(prediction[0],probability)
            json["prediction"] = prediction[0]
            json["probability"] = probability
            add_record(json)
            print "Received data {}".format(json["object_id"])
            current_object = json["object_id"]
        else:
            print "duplicate"
        time.sleep(1)

def load_model():
    '''Loads pickle file as model
    '''
    with open('model.p') as f:
        m = pickle.load(f)
    return m

#placeholder for later predict function when pickle file loads it quickly
def predict(json):
    # from IPython import embed
    # embed()
    df = pd.DataFrame.from_dict([json])

    # df = pd.read_json(datapoint)
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
    return model.predict(X)

#Runs
model = load_model()
pull_loop()
