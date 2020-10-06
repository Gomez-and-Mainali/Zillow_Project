import wrangle

import acquire


def prep_data():
    zillow = acquire.get_data()
    
    zillow = zillow[~zillow.fullbathcnt.isna()]
    
    zillow = zillow[~zillow.finishedsquarefeet12.isna()]
    
    zillow = zillow[~zillow.lotsizesquarefeet.isna()]
    
    zillow = zillow[~zillow.regionidzip.isna()]
    
    zillow = zillow.drop(columns = ['propertylandusedesc', 'transactiondate', 'id', 'parcelid', 'calculatedbathnbr])
    
    
    zillow = zillow.rename(columns = {'bathroomcnt':'numberofbathrooms', 'bedroomcnt':'numberofbedrooms', 
                         'regionidcounty':'countyid', 'regionidzip':'zipcode', 'finishedsquarefeet12':'size_in_squarefeet', 
                        'fullbathcnt':'fullbath', 'lotsizesquarefeet':'lotsize', 'taxamount': 'tax', 
                        'taxvaluedollarcnt':'property_value'})
    
    q1 = zillow.property_value.quantile(0.25)
    
    q3 = zillow.property_value.quantile(0.75)

    iqr = q3-q1

    upper_outlier_mark = q3 + (1.5 * iqr)

    zillow = zillow[zillow.property_value < upper_outlier_mark]
                                    
    zillow.fips = zillow.fips.astype(int)

    zillow = zillow.replace({'fips':{6037: 'LA', 6059: 'Orange', 6111: 'Ventura'}})

    zillow = zillow.rename(columns = {'fips': 'County'})                               
    
    
    dummies = pd.get_dummies(zillow.County)
                                    
    zillow = pd.concat([zillow, dummies], axis = 1)
                                    
    zillow = zillow.drop(columns = 'County')
                                    
                                     
                                    
    train, test, validate = wrangle.split_data(zillow)
    
    
    return train, test, validate