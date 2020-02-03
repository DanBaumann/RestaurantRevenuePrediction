import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def read_csv(filename):
    data = pd.read_csv(filename, index_col=0)
    return data

def X_and_y(data):
    """
    Retrieves target and predictor variables
    Arguments:
    data: the dataframe
    """
    y = data['revenue']
    X = data.drop('revenue', axis=1)
    return y, X

def min_max_scaling(X, y):
    """
    Scales the predictor variables using Min Max Scaler from sklearn.
    Then combines the scaled data with the target variable
    Arguments:
    X: the predictor variables
    y: target variable
    """
    minmax = MinMaxScaler()
    X_scaled = pd.DataFrame(data=minmax.fit_transform(X), columns=X.columns,
                            index=X.index)
    # will not scale the output, but will now merge data
    df_scaled = X_scaled.join(y)
    return df_scaled

def train_test_split(data):
    """
    Splits the training and testing scaled dataset, and then applying the 
    square root to the target variable so as to reduce the impact of outliers
    Arguments:
    data: the dataframe
    """
    train = data.loc[pd.notnull(data['revenue'])]
    test = data.loc[pd.isnull(data['revenue'])].drop('revenue', axis =1)
    
    y = train['revenue'].apply(np.sqrt)
    X = train.drop('revenue', axis=1)
    
    return test, y, X



