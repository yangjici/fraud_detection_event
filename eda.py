import pandas as pd


df = pd.read_json('data.json')
# df.to_csv('data.csv', sep='\t')
df.info()
'''
Total entries: 14337
Missing values:
- has_header (8928 non-null)

'''

df.head(10)
df.describe()
'''
acct_type: 'fraudster_event', 'premium'
description:
    - fraud: html url <a href=...
    - non-fraud: html text

email add:
    - fraud: gmail
    - non-fraud: non-personal email domain
user age:
    - both: max (3794), min (13)


'''
df['acct_type'].unique()

'''
array([u'fraudster_event', u'premium', u'spammer_warn', u'fraudster',
       u'spammer_limited', u'spammer_noinvite', u'locked', u'tos_lock',
       u'tos_warn', u'fraudster_att', u'spammer_web', u'spammer'], dtype=object)
'''
df.groupby('acct_type')['user_created'].count()

df[(df['acct_type']=='locked')].head()

fraud_flags = ['fraudster_event', 'fraudster', 'fraudster_att']


df['Fraud'] = df['acct_type'].map(lambda x: 1 if x in fraud_flags else 0)

df.corr().Fraud

'''
approx_payout_date   -0.042553
body_length          -0.118308
channels             -0.165358
delivery_method      -0.194046
event_created        -0.006436
event_end            -0.042553
event_published      -0.077322
event_start          -0.044995
fb_published         -0.099143
gts                  -0.017875
has_analytics        -0.084626
has_header           -0.082101
has_logo             -0.169485
name_length          -0.158447
num_order            -0.078008
num_payouts          -0.083433
object_id             0.026721
org_facebook         -0.181792
org_twitter          -0.205692
sale_duration        -0.179512
sale_duration2       -0.179550
show_map             -0.076217
user_age             -0.215929
user_created          0.184360
user_type            -0.213911
venue_latitude        0.010126
venue_longitude       0.066057
Fraud                 1.000000

'''

def kde_plot(df, label_column_name, feature_column_name, title):
    df[df[label_column_name]==1][feature_column_name].plot.kde(label=label_column_name)
    df[df[label_column_name]==1][feature_column_name].plot.kde(label=label_column_name)
    plt.title(title)
    plt.legend()
    plt.show()
