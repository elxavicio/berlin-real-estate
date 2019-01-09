from pandas import DataFrame, read_csv
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import random


airbnb_file = r'airbnb_listings.csv'
df = pd.read_csv(airbnb_file)
print(df.columns)

print(df.room_type.unique())

### Apply filters
df = df[(df.property_type == "Apartment") & (df.room_type == "Entire home/apt") & (df.bedrooms < 3)]
df['price'] = df['price'].apply(lambda x : x.replace("$",""))
df['price'] = df['price'].apply(lambda x : float(x.replace(",","")))

# price_column = df['price']
# df = df[((price_column > price_column.quantile(.05)) & (price_column < price_column.quantile(.95)))]
print(df)
print(df['price'].dtype)
print(df['latitude'].dtype)
print(df['longitude'].dtype)
print(df['bedrooms'].dtype)

X = df[['latitude','longitude','bedrooms']]
Y = df[['price']]

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# prediction with sklearn
bedrooms = 2
latitude = 52.524322269
longitude = 13.413731897
price = 85

print( regr.predict([[latitude ,longitude, bedrooms]]))

# obtaining nightly price per property

sale_listings_file = r'sale_listing.csv'
df = pd.read_csv(sale_listings_file)
df['bedrooms'] = df['bedrooms'].apply(lambda x : float(x.replace(",",".")))
df['nightly_price'] = df.apply(lambda row: float(regr.predict([[row['latitude'] ,row['longitude'], row['bedrooms']]])), axis=1)
df['latitude'] = df.apply(lambda x: x['latitude']+(random.random()*0.0001), axis=1)
df['longitude'] = df.apply(lambda x: x['longitude']+(random.random()*0.0001), axis=1)
df.to_csv('regression_output.csv')
