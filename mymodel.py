from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge
from sklearn import preprocessing
import sklearn.metrics as metrics
from sklearn import linear_model
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import pickle 
# import seaborn as sns

def preprocess(df):
    # df = df.dropna()
    # df = df[df["Crop"]=="Avocados"]
    # df = df.drop(columns="Crop", axis=1)
    # df = df.drop(columns="Year", axis=1)
    df['Export Quantity'] = df['Export Quantity'].interpolate(method='linear', limit_direction='backward', axis=0)
    scaler = preprocessing.StandardScaler()
    scal_feat = ['Temperature (Avg)','Precipitation','Export Quantity','Fertilizer Usage']
    df[scal_feat]=scaler.fit_transform(df[scal_feat].to_numpy())
    feat = scal_feat + ["Crop"]
    X = df[feat].copy(deep=True)
    X = pd.get_dummies(X, columns = ['Crop'])
    y = df['Yield'].copy(deep=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 13)

    return X_train, X_test, y_train, y_test, X


def compute_scores(y_test, y_pred):
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse) 
    r2 = metrics.r2_score(y_test, y_pred)
    print("MAE : ",mae)
    print("MSE : ",mse)
    print("RMSE : ",rmse)
    print("R2 : ",r2)

df = pd.read_csv("DryBeanDataset/crop_yield_data.csv")

df = df.drop(columns=["Year"], axis =1 )    

X_train, X_test, y_train, y_test, X = preprocess(df)

dt_regression = DecisionTreeRegressor()
dt_regression.fit(X_train, y_train)
y_pred_dt = dt_regression.predict(X_test)
compute_scores(y_test, y_pred_dt)

pickle.dump(dt_regression, open("model.pkl","wb"))

