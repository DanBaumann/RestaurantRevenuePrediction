import pandas as pd
import datetime

def read_train_and_test(train_filename, test_filename):
    train = pd.read_csv(train_filename, index_col=0, parse_dates=[1])
    test = pd.read_csv(test_filename, index_col=0, parse_dates=[1])
    
    data = pd.concat((train, test), ignore_index=True, sort=False)
    data['Open Date'] = data['Open Date'].apply(pd.to_datetime)
    return train, test, data

def col_names(data):
    data.rename(columns={'Open Date': 'open_date', 'City':'city', 'City Group':'city_type', 
                         'Type':'type'}, inplace=True)
    return data

def months_since_opening(data):
    last_open_date = data['open_date'].max()
    data['open_date'] = last_open_date - data['open_date']
    data['open_date'] = data['open_date'].dt.days + 365
#     dividing average month length of 30.4 and rounding up
    data['open_date'] = round(data['open_date']/30.4)
    data['open_date'] = data['open_date'].astype(int)
    data.rename(columns={'open_date':'months_since_opening'}, inplace=True)
    return data

def zeros_plot(data):
    plt.figure(figsize=(20,9))

    plt.subplot(1, 2, 1)
    train_distribution = data['zeros'].loc[pd.notnull(data['revenue'])].value_counts()
    train_distribution.plot(kind='bar', color='b')
    plt.title("Training Distribution of Zeros")
    plt.xlabel("Variable")

    plt.subplot(1, 2, 2)
    test_distribution = data['zeros'].loc[pd.isnull(data['revenue'])].value_counts()
    test_distribution.plot(kind='bar', color='r')
    plt.title("Test Distribution of Zeros")
    plt.xlabel("Variable")
    
def city_type_dummies(data):
    data = pd.get_dummies(data, columns=['city_type'], prefix='ct', drop_first=True)
    return data

def category_lists(data):
    groupby = data.groupby('city')['revenue'].mean()
    low, low_mid, high_mid, high = list(), list(), list(), list()
    
    for i, j in enumerate(groupby):
        if j < groupby.quantile(0.25):
            low.append(groupby.index[i])
        elif j < groupby.quantile(0.5):
            low_mid.append(groupby.index[i])
        elif j < groupby.quantile(0.75):
            high_mid.append(groupby.index[i])
        elif j <= groupby.quantile(1):
            high.append(groupby.index[i])

    def assert_type(i):
        if i in low:
            return 'low'
        if i in low_mid:
            return 'low_mid'
        if i in high_mid:
            return 'high_mid'
        else:
            return 'high'
        
    data['city_price'] = data['city'].apply(lambda x: assert_type(x))
    
    data = pd.get_dummies(data, prefix = 'city', columns=['city_price'], drop_first=True)
    
    del data['city']
    
    return data, low, low_mid, high_mid, high 

def restaurant_type_dummies(data):
    data = pd.get_dummies(data, columns=['type'], prefix='rt', drop_first=True)
    return data

def one_hot_encode_obfuscated(data):
    for col in data.columns:
        if col[0]=='P':
            data = pd.get_dummies(data, columns=[col], prefix=col, drop_first=True)
    return data




    
    