import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import pickle 

# import seaborn as sns

# def beans_prediction(beans):
beansdata = pd.read_excel("Dry_Bean_Dataset.xlsx")

X_iris = beansdata.drop(['Class',"Area","MajorAxisLength","MinorAxisLength",
                        "AspectRation","Eccentricity","EquivDiameter","ShapeFactor1","ShapeFactor2","ShapeFactor3",
                        "ShapeFactor4","ConvexArea"], axis=1)
y_iris = beansdata["Class"]

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

print(Xtrain.shape, "sdfghjfghjhj", ytrain.shape)
print(Xtest.shape, "testttttttt", ytest.shape)
from sklearn.naive_bayes import GaussianNB # 1. choose model class
modelGau = GaussianNB() # 2. instantiate model
modelGau.fit(Xtrain, ytrain) # 3. fit model to data
pickle.dump(modelGau, open("model.pkl","wb"))
model = pickle.load(open("model.pkl", "rb"))

