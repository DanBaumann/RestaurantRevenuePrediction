from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, KFold, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

class Baseline_model(object):
    
    def linear_regression(self, X, y, test):
        model = LinearRegression()
        model.fit(X, y)
        train_predictions = pd.DataFrame(columns=['Prediction'], index=X.index, data=model.predict(X))
        print("Training MSE: {}".format(mean_squared_error(y, model.predict(X))))
        print("Training RMSE: {}".format(np.sqrt(mean_squared_error(y, model.predict(X)))))
        return train_predictions
        
class Ridge_model(object):
    
    def grid_search(self, model, grid, X, y):
        grid_search = GridSearchCV(estimator=model, param_grid=grid, 
                                   scoring='neg_mean_squared_error')
        grid_search.fit(X, y)
        print("Best Parameters found with GridSearchCV:")
        print(grid_search.best_params_)
        return grid_search.best_params_
        
    def save_best_params(self, model, best_params):
        model.set_params(**best_params)
        model.fit(X, y)
        print("Training MSE: {}".format(mean_squared_error(y, model.predict(X))))
        print("Training RMSE: {}".format(np.sqrt(mean_squared_error(y, model.predict(X)))))
        
        
class XGboost_regression(object):

    def grid_search(self, model, grid, X, y):
        grid_search = GridSearchCV(estimator=model, param_grid=grid,
                                   scoring='neg_mean_squared_error', verbose=1)
        grid_search.fit(X, y)
        print("Best Parameters found with GridSearchCV:")
        print(grid_search.best_params_)
        return grid_search.best_params_
    
    def save_best_params(self, model, grid_search):
        model.set_params(**grid_search.best_params_)
        model.fit(X, y)
       