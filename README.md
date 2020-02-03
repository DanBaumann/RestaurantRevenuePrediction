<h1 align='center'>Restaurant Revenue Prediction</h1>
<br>
<h3 align='center'>Daniel Baumann</h1>
<br>
____________________________________________________________________________________________________________________________
<h3 align='center'>The Problem</h3>

TFI is a company behind some of the world's most well-known brands, including Burger King, Popeyes etc. It is in their interest to find and develop new restaurant sites which will ultimately maximise their revenue and profitablity.
For this reason, they decided to open a competition on Kaggle, where entrants were tasked with predicting the revenue of restaurants given a multitude of factors
<br>
____________________________________________________________________________________________________________________________
<h3 align='center'>Project Objectives</h3>

The aim of this project is to create a model which can accurately predict the revenue of restaurant sites. This would allow TFI to invest with more confidence in given areas. <br> The dataset includes the following variables:

* The opening date of the restaurant
* The city it is located in
* The type of city (big or other)
* The type of restaurant (food court, drive thru etc)
* 37 categories of obfuscated data which include demographic, real estate and commercial factors
* The target variable: revenue
<br>
____________________________________________________________________________________________________________________________
<h3 align='center'>Methods Used</h3>

* Data visualisation
* Feature engineering
* Linear regression modelling (Ridge, XGBoost)
* Libraries used:
  * matplotlib, seaborn, sklearn, pandas, xgboost
<br>
____________________________________________________________________________________________________________________________
<h3 align='center'>Project Contents</h3>
<br>
The project contains the following:

* Exploratory data analysis and data preprocessing
  * Inspecting each variable and the effect on revenue
  * Creating dummy variables for categorical data
  * Creating new columns based on the relative price of cities
  * Data visualisation 
* Creating a baseline model
  * Using simple multi-variate linear regression to derive a baseline model
* Using grid search methods to find the optimal Ridge regression
  * Displaying a visualisation of training predictions compared with actual data
* Using grid search methods to find the optimal XGBoost regression model
  * Also displaying training versus xgboost predictions
* Showing scores of competition submission 
<br>
