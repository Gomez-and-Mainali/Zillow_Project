#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from env import host, user, password
import os


# In[2]:


# Create a function that creates a a url for accessing the database

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[3]:


# query = sql statement to get the desired data
def get_data():
    '''This function reads in a sql query and the retrieves the data from the database using the get connection function. Converts the data in csv file and returns it'''
    
    query = '''select  p2.id, p2.parcelid, p2.bathroomcnt, p2.bedroomcnt, p2.calculatedbathnbr, p2.regionidcounty, p2.regionidzip,
p2.finishedsquarefeet12, p2.fips, p2.fullbathcnt,p2.lotsizesquarefeet, plt.propertylandusedesc, p17.transactiondate,
p2.taxamount, p2.taxvaluedollarcnt
from properties_2017 p2
join propertylandusetype plt on plt.propertylandusetypeid = p2.propertylandusetypeid
join predictions_2017 p17 on p17.parcelid = p2.parcelid
where (plt.propertylandusedesc = 'Single Family Residential') and (p2.taxamount is not NULL) and
((p17.transactiondate like '2017-05-%%') OR (p17.transactiondate like '2017-06-%%'))
'''
    zillow = pd.read_sql(query, get_connection('zillow'))
    
    zillow.to_csv('zillow_csv')
    
    return zillow


# In[8]:


# creating a cache so that we wont have to run the whole get data every time
def get_zillow_data(cached = False):
    '''
    This function reads in titanic data from Codeup database if cached == False 
    or if cached == True reads in titanic df from a csv file, returns df
    '''
    if cached or os.path.isfile('zillow.csv') == False:
        zillow = get_data()
    else:
        zillow = pd.read_csv('zillow.csv', index_col=0)
    return zillow


# In[ ]:




