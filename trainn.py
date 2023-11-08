# -*- coding: utf-8 -*-
"""Copy of MidTerm_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KcoazKwinnmO_qve1fkW0PzMzsBkyxb-
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

dfa=pd.read_csv('https://raw.githubusercontent.com/anandaiml19/ML_ZoomCamp_2023/main/Cleaned_dataset.csv')

dfa.head()

dfa.info()

"""**Data Cleaning and Preprocessing**"""

dfa['Date_of_journey']=dfa['Date_of_journey'].astype('datetime64[ns]')

dfa['day_of_month']=dfa['Date_of_journey'].dt.strftime('%d')

dfa.head()

dfa[['day_of_month']]=dfa[['day_of_month']].astype('int')

dfa.info()

dfa.dtypes

datecols= list(dfa.dtypes[dfa.dtypes=='datetime64[ns]'].index)

datecols

dfa.columns=dfa.columns.str.lower()

dfa.columns

categoricalsn= list(dfa.dtypes[dfa.dtypes=='object'].index)

categoricalsn

newcols=['journey_day','airline','class','source','departure','total_stops','arrival','destination','day_of_month', 'days_left', 'duration_in_hours', 'fare']

len(newcols)

dfa.corr()

del dfa['flight_code']

dfa.head()

"""**Model Training and Prediction**"""

from sklearn.model_selection import train_test_split

import xgboost
xgboost.__version__

dfa_full_train,dfa_test=train_test_split(dfa,test_size=0.2,random_state=42)

len(dfa_full_train),len(dfa_test)

dfa_train,dfa_val=train_test_split(dfa_full_train,test_size=0.25,random_state=42)

len(dfa_train),len(dfa_val),len(dfa_test)

dfa_train=dfa_train.reset_index(drop=True)
dfa_val=dfa_val.reset_index(drop=True)
dfa_test=dfa_test.reset_index(drop=True)

y_train=dfa_train.fare.values
y_val=dfa_val.fare.values
y_test=dfa_test.fare.values

del dfa_train["fare"]
del dfa_val["fare"]
del dfa_test["fare"]

category_new=['journey_day','airline','class','source','departure','total_stops','arrival','destination']

"""**One hot Encoding**"""

from sklearn.feature_extraction import DictVectorizer

numericc= ['day_of_month', 'days_left', 'duration_in_hours']

dv=DictVectorizer(sparse=False)
train_dict=dfa_train[category_new+numericc].to_dict(orient='records')
x_train=dv.fit_transform(train_dict)

val_dict=dfa_val[category_new+numericc].to_dict(orient='records')
x_val=dv.transform(val_dict)

"""**XG Boost regressor**"""

import xgboost as xgb

from xgboost import XGBRegressor

xgbmodel =  XGBRegressor()

from sklearn.metrics import mean_squared_error, r2_score

xgbmodel.fit(x_train,y_train)

y_predxgb=xgbmodel.predict(x_val)

print("R2 score is",r2_score(y_val,y_predxgb))

print("Root mean squared error",np.sqrt(mean_squared_error(y_val,y_predxgb)))

"""**Hyperparamter Tuning - XG Boost Regressor**"""

xgbmodel_hpt =  XGBRegressor(learning_rate=0.17,max_depth=15,min_child_weight=7)

xgbmodel_hpt.fit(x_train,y_train)

y_predxgbhpt=xgbmodel_hpt.predict(x_val)

print("R2 score is",r2_score(y_val,y_predxgbhpt))

print("Root mean squared error",np.sqrt(mean_squared_error(y_val,y_predxgbhpt)))

"""**Best Model**

Based on the Analysis of different models viz., linear and tree based model with Hyperparamter tuning. The XG Boost regressor model delivered higher R2 score with lower Root mean squared error. The final model chosen for this project is **XGB Regressor**.
"""

import pickle

from joblib import dump

with open('dvf.bin','wb') as f_out1:
  pickle.dump(dv,f_out1)

with open('modelf.pkl','wb') as f_out2:
  pickle.dump(xgbmodel_hpt,f_out2)

xgbmodel_hpt.save_model("model.json")

dump(xgbmodel_hpt,"xgbjl.pkl")