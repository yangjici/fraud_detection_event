
import pandas as pd
import numpy as np
import datetime


def make_price(row):
    s2=np.array([0,0,0,0]).reshape(1,4)
    if (row!= []):
        if ('cost' in row[0]):
            prices=[int(tic['cost']) for tic in row]
            total = np.sum([int(tic['quantity_total']) for tic in row  ])
            s1 = np.array([len(row),min(prices),max(prices),total],).reshape(1,4)
            return s1
    else:
        return s2

def add_price(df):
    price_features = np.array([0,0,0,0]).reshape(1,4)

    for i in df.ticket_types:
        price = make_price(i)
        price_features = np.append(price_features,price,axis=0)


    price_features = pd.DataFrame(price_features[1:,],columns=['types_of_tickets','min_price','max_price','ticket_num'])

    df = pd.concat([df,price_features],axis=1)
    return df




def make_time(t):
    return datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

def payout_info(row):
    no_payout=np.array([0,0]).reshape(1,2)
    if (row!=[]):
        num = len(row)
        if 'created' in row[0]:
            time_list =list(set([pay['created'] for pay in row]))
            time_object = sorted([make_time(t) for t in time_list])
            time_int = [time_object[n]-time_object[n-1] for n in range(1,len(time_object))]
            minutes_int = np.array([dt.seconds//60 for dt in time_int])
            try:
                median_minute = np.min(minutes_int)
            except ValueError:
                return np.array([1,0]).reshape(1,2)
            return np.array([num,median_minute]).reshape(1,2)
    else:
        return no_payout


def make_payout(df):
    payout_features = np.array([0,0]).reshape(1,2)

    for i in df.previous_payouts:
        payout = payout_info(i)
        payout_features = np.append(payout,payout_features,axis=0)

    payout_features = pd.DataFrame(payout_features[1:,],columns=['number_previous_payout','median_min_interval'])


    df = pd.concat([df,payout_features],axis=1)
    return df
