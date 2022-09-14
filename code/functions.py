# -- Imports --
import pandas as pd
import numpy as np

# Import and clean data
def import_and_clean_data(filepath):
    df = pd.read_csv(filepath).dropna()
    
    # Cleaning
    highquant_living = df['sqft_living'].quantile(0.99)
    highquant_lot = df['sqft_lot'].quantile(0.99)
    highquant_basement = df['sqft_basement'].quantile(0.99)
    highquant_patio = df['sqft_patio'].quantile(0.99)
    highquant_garage = df['sqft_garage'].quantile(0.99)
    
    df = df[df['sqft_living'] < highquant_living]
    df = df[df['sqft_living'] > 100] # Gets rid of abnormally low sqfts
    
    df = df[df['sqft_lot'] < highquant_lot]
    
    df = df[df['sqft_basement'] < highquant_basement]
    
    df = df[df['sqft_patio'] < highquant_patio]
    
    df = df[df['sqft_garage'] < highquant_garage]
    
    # Feature engineering
    df['age'] = 2021 - df['yr_built']

    df['bath_to_bed'] = df['bathrooms'] / df['bedrooms']
    df = df.replace([np.inf, -np.inf], df['bath_to_bed'].median()).fillna(df['bath_to_bed'].median()) # Replaces inf/-inf/nan values with median

    df['zip'] = df.address.apply(lambda x: x[x.rfind(',') - 5:x.rfind(',')])
    
    df['condition'] = df['condition'].replace({'Poor': 1, 
                                               'Fair': 2, 
                                               'Average': 3, 
                                               'Good': 4, 
                                               'Very Good': 5})
    df['grade'] = df['grade'].replace({'1 Cabin': 1, 
                                       '2 Substandard': 2, 
                                       '3 Poor': 3, 
                                       '4 Low': 4, 
                                       '5 Fair': 5,
                                       '6 Low Average': 6,
                                       '7 Average': 7,
                                       '8 Good': 8,
                                       '9 Better': 9,
                                       '10 Very Good': 10,
                                       '11 Excellent': 11,
                                       '12 Luxury': 12,
                                       '13 Mansion': 13,
                                      })
    
    return df