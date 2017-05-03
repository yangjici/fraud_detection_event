import pandas as pd
import numpy as np

#break out the ticket types column
def make_column(row):
    s2=np.array([None,None,None]).reshape(1,3)
    if (row!= []):
        if ('cost' in row[0]):
            prices=[int(tic['cost']) for tic in row]
            s1 = np.array([len(row),min(prices),max(prices)]).reshape(1,3)
            return s1
    else:
        return s2
price_features = np.array([0,0,0]).reshape(1,3)
for i in df.ticket_types:
    price = make_column(i)
    price_features = np.append(price_features,price,axis=0)
price_features = pd.DataFrame(price_features[1:,],columns=['number_tickets','min_price','max_price'])
df_price = pd.concat([df,price_features],axis=1)

#create new column for popularity of event
df_price['country']=df_price['country'].fillna(0)


df_price['popularity'] =

'''
Columns that currently have some null values:
country
delivery_method
event_published
has_header
org_facebook
org_twitter
sale_duration
venue_country
venue_latitude
venue_longitude
venue_name
venue_state
'''
