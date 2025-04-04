
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
import os
import pickle
import warnings

warnings.filterwarnings('ignore')

csv_path = os.path.join(os.path.dirname(__file__), 'Zomato_df.csv')
df=pd.read_csv(csv_path)

df.drop('Unnamed: 0',axis=1,inplace=True)
print(df.head())
x=df.drop('rate',axis=1)
y=df['rate']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=10)


#Preparing Extra Tree Regression
from sklearn.ensemble import  ExtraTreesRegressor
ET_Model=ExtraTreesRegressor(n_estimators = 120)
ET_Model.fit(x_train,y_train)


y_predict=ET_Model.predict(x_test)

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
pickle.dump(ET_Model, open(model_path, 'wb'))
model=pickle.load(open('model.pkl','rb'))
print(y_predict)