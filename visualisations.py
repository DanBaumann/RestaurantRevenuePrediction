import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
plt.style.use('ggplot')
def open_dates_scatterplot(data):
    plt.figure(figsize=(15,9))
    sns.scatterplot(x='open_date', y='revenue', data=data)
    plt.title('How revenue changes with opening date')
    plt.xlabel('Open Date')
    plt.ylabel('Revenue')
    
def month_distplot(data):
    plt.figure(figsize=(15,9))
    sns.distplot(data['months_since_opening'])
    plt.title('Distribution Plot of Restaurant Age')
    plt.xlabel('Months Since Opening', fontdict={'fontsize':15})
    plt.ylabel('Probability Distribution', fontdict={'fontsize':15})
    
def month_barplot(data):
    plt.figure(figsize=(15,9))
    sns.barplot(x='bins', y = 'revenue', data=data, ci=None)
    plt.title('How Revenue differs with Restaurant Age')
    plt.xlabel('Months Since Opening', fontdict={'fontsize':15})
    plt.ylabel('Revenue', fontdict={'fontsize':15})
        
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
    plt.xlabel("Variable", fontdict={'fontsize':15})
    
def city_type_barplot(data):
    plt.figure(figsize=(20,9))

    plt.subplot(1, 2, 1)
    train_city_type = data['city_type'].loc[pd.notnull(data['revenue'])].value_counts()
    train_city_type.plot(kind='bar', color='b')
    plt.title('Training Distribution of City Type', fontdict={'fontsize':25})
    plt.xlabel('City Type', fontdict={'fontsize':15})

    plt.subplot(1, 2, 2)
    test_city_type = data['city_type'].loc[pd.isnull(data['revenue'])].value_counts()
    test_city_type.plot(kind='bar', color='r')
    plt.title('Test Distribution of City Type', fontdict={'fontsize':25})
    plt.xlabel('City Type', fontdict={'fontsize':15})
    
def city_type_revenue_barplot(data):
    plt.figure(figsize=(15,9))
    sns.barplot(x='city_type', y='revenue', data=data, ci=None)
    plt.title('Revenue by City Type', fontdict={'fontsize':25})
    plt.ylabel('Revenue', fontdict={'fontsize':15})
    plt.xlabel('City Type', fontdict={'fontsize':15})
    
def major_city_revenues_barplot(data):
    plt.figure(figsize=(15,9))
    sns.barplot(x='city', y='revenue', data=data.sort_values('revenue', ascending=False), ci=None)
    plt.title('Revenue by Major City', fontdict={'fontsize':25})
    plt.xlabel('Major City', fontdict={'fontsize':15})
    plt.ylabel('Revenue', fontdict={'fontsize':15})
    
def revenue_by_city_barplot(data):
    plt.figure(figsize=(15,9))
    flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    sns.barplot(x='revenue', y='city', data=data.sort_values('revenue', ascending=False),
                orient='H', ci=None, palette=flatui)
    plt.title('Average Revenue by City', fontdict={'fontsize':25})
    plt.ylabel('City', fontdict={'fontsize':15})
    plt.xlabel('Revenue', fontdict={'fontsize':15})
     
def restaurant_type_barplot(data):
    plt.figure(figsize=(20,9))

    plt.subplot(1, 2, 1)
    train_restaurant_type = data['type'].loc[pd.notnull(data['revenue'])].value_counts()
    train_restaurant_type.plot(kind='bar', color='b')
    plt.title('Training Distribution of Restaurant Type', fontdict={'fontsize':25})
    plt.ylabel('City', fontdict={'fontsize':15})
    plt.xlabel('Revenue', fontdict={'fontsize':15})
    
    plt.subplot(1, 2, 2)
    test_restaurant_type = data['type'].loc[pd.isnull(data['revenue'])].value_counts()
    test_restaurant_type.plot(kind='bar', color='r')
    plt.title('Testing Distribution of Restaurant Type', fontdict={'fontsize':25})
    plt.ylabel('City', fontdict={'fontsize':15})
    plt.xlabel('Revenue', fontdict={'fontsize':15})
    
def revenue_by_restaurant_barplot(data):
    plt.figure(figsize=(15,9))
    flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    sns.barplot(x='revenue', y='type', data=data.sort_values('revenue', ascending=False),
            ci=None, palette=flatui)
    plt.title('Average Revenue by Restaurant Type', fontdict={'fontsize':25})
    plt.ylabel('Restaurant Type', fontdict={'fontsize':15})
    plt.xlabel('Revenue', fontdict={'fontsize':15})
    
def revenue_distplot(data):
    plt.figure(figsize=(15,9))
    sns.distplot(data)
    plt.title('Distribution Plot of Revenue')
    plt.xlabel('Revenue', fontdict={'fontsize':15})
    plt.ylabel('Probability Distribution', fontdict={'fontsize':15})

def correlation_matrix(data):
    sns.set(style='white')
    corr = data.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)]=True
    f, ax = plt.subplots(figsize=(15,15))
    
    cmap = sns.diverging_palette(200, 15, as_cmap=True)
    
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
               square=True, linewidths=.5, cbar_kws={'shrink':.5})

