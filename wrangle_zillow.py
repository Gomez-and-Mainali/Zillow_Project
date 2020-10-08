#!/usr/bin/env python
# coding: utf-8




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing
from sklearn.model_selection import train_test_split




def split_data(df):
    
    '''Takes in a dataframe and splits into a train, test, and validate and returns a train, test,  and validate dataframe'''
    
    train_validate, test = train_test_split(df, test_size = .20, random_state = 123)

    train, validate = train_test_split(train_validate, test_size = 0.20, random_state = 123)

    return train, test, validate




def scale_data(train, test, validate, scaler, cols_to_scale):
    '''Intakes train, test, validate dataset, scaling methond, and the list of columns to scale
    and returns train, test, validate dataset with scaled data added to new columns'''

    
    new_cols = [col + "_scaled" for col in cols_to_scale]
    
    
    scaler = scaler.fit(train[cols_to_scale])
    
    train = pd.concat([train, pd.DataFrame(scaler.transform(train[cols_to_scale]), 
                                           index = train.index, columns = new_cols)], axis = 1)
    
    train_scaled = train.drop(columns = cols_to_scale)
    
    
    test =  pd.concat([test, pd.DataFrame(scaler.transform(test[cols_to_scale]), 
                                           index = test.index, columns = new_cols)], axis = 1)
    
    
    test_scaled = test.drop(columns = cols_to_scale)
    
    validate =  pd.concat([validate, pd.DataFrame(scaler.transform(validate[cols_to_scale]), 
                                           index = validate.index, columns = new_cols)], axis = 1)
     
        
    validate_scaled = validate.drop(columns = cols_to_scale)
                      
    return train_scaled, test_scaled, validate_scaled     







