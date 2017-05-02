import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats as scs
import matplotlib.pyplots as plt
import statsmodels.api as sm

 data = pd.read_json('data.json')
 df = pd.DataFrame(data)

y = df['acct_type']
X = df.drop('acct_type', axis=1)

df.isnull().values.any()
df.describe()
df.info()
df.acct_type.unique()

 fraud = df.loc[df['acct_type'] == fraudster]
 #Fraud types: fraudster_event, premium, spammer_warn, fraudster, spammer_limited, fraudster_att, spammer_web, spammer

#Currency type: USD,EUR,CAD,GBP,AUD,NZD,MXN


acct_type             14337 non-null object
approx_payout_date    14337 non-null int64
body_length           14337 non-null int64
channels              14337 non-null int64
country               14256 non-null object
currency              14337 non-null object
delivery_method       14321 non-null float64
description           14337 non-null object
email_domain          14337 non-null object
event_created         14337 non-null int64
event_end             14337 non-null int64
event_published       14238 non-null float64
event_start           14337 non-null int64
fb_published          14337 non-null int64
gts                   14337 non-null float64
has_analytics         14337 non-null int64
has_header            8928 non-null float64
has_logo              14337 non-null int64
listed                14337 non-null object
name                  14337 non-null object
name_length           14337 non-null int64
num_order             14337 non-null int64
num_payouts           14337 non-null int64
object_id             14337 non-null int64
org_desc              14337 non-null object
org_facebook          14278 non-null float64
org_name              14337 non-null object
org_twitter           14278 non-null float64
payee_name            14337 non-null object
payout_type           14337 non-null object
previous_payouts      14337 non-null object
sale_duration         14182 non-null float64
sale_duration2        14337 non-null int64
show_map              14337 non-null int64
ticket_types          14337 non-null object
user_age              14337 non-null int64
user_created          14337 non-null int64
user_type             14337 non-null int64
venue_address         14337 non-null object
venue_country         13261 non-null object
venue_latitude        13261 non-null float64
venue_longitude       13261 non-null float64
venue_name            13261 non-null object
venue_state           13261 non-null object
