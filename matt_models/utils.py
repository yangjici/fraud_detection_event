'''
Clean up the data
'''
import pandas as pd
import numpy as np


keep = ['acct_type','channels','description','gts','name','num_payouts','ticket_types','user_age','user_type']
org_payee = ['org_name','org_name','payee_name','payout_type','previous_payouts']


def get_df(path='data/data.json'):
    df = pd.read_json(path)
    return df


def drop_columns(in_df, cols):
    df = in_df.copy()
    for col in cols:
        if col in df.columns:
                df = df.drop(col, axis=1)
    return df


def keep_columns(in_df, cols):
    df = in_df.copy()
    return df[cols]


def get_rid_of_tos_lock(in_df):
    df = in_df.copy()
    df = df[df['acct_type'] != 'tos_warn']
    df = df[df['acct_type'] != 'tos_lock']
    df = df[df['acct_type'] != 'locked']
    return df


def make_premium_labels(in_df):
    df = in_df.copy()
    labels = df['acct_type']
    labels = np.where(df['acct_type'] == "premium", 0, 1)
    del df['acct_type']
    return df, labels


def make_fraud_labels(df):
    df = in_df.copy()
    df['fraud'] = [1 if x in ['fraudster', 'fraudster_event', 'fraud_att'] else 0 for x in df.acct_type]
    y = df['fraud']
    del df['acct_type']
    return df, y


def get_ticket_types_df(in_df):
    dfc = in_df.copy()
    tix = dfc.ticket_types

    l = []
    for i in xrange(tix.shape[0]):
        #print i
        fraud = dfc['fraud'].iloc[i]

        for ticket_listing in xrange(len(tix.iloc[i])):
            new_row = [fraud]
            for k, v in tix.iloc[i][ticket_listing].iteritems():
                new_row.append(v)

            l.append(new_row)

    cols = ['fraud'] + tix[0][0].keys()
    tix_df = pd.DataFrame(l,columns=cols)
    return tix_df
