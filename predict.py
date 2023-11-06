#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install Pipenv


# In[2]:


#get_ipython().system('Pipenv install ipykernel')


# In[3]:


#get_ipython().system('Pipenv install python==3.10.12')


# In[4]:


#get_ipython().system('Pipenv install pandas==1.5.3 numpy==1.23.5 seaborn==0.12.2 matplotlib==3.7.1 pickle==4.0')


# In[5]:


#get_ipython().system('Pipenv install Scikit-Learn==1.2.2')


# In[6]:


#get_ipython().system('Pipenv install flask')


# In[7]:


#pwd


# In[8]:


#get_ipython().system('Pipenv install waitress')


# In[32]:


#get_ipython().system('Pipenv install xgboost==2.0.1')


# In[3]:


import xgboost
import sklearn

# In[33]:


from sklearn.feature_extraction import DictVectorizer


# In[34]:


dv = DictVectorizer(sparse=False)


# In[35]:
import pickle
from flask import Flask
from flask import request
from flask import jsonify


# In[16]:


#input_file1='modelf.sav'


# In[36]:


input_file2='dvf.bin'


# In[18]:


'''def load_pkls(filename):
    with open(input_file1,'rb') as f_in:
        obj=pickle.load(f_in)
    return obj'''


# In[21]:


'''model=load_pkls('modelf.sav')'''


# In[37]:


with open(input_file2,'rb') as f_inn:
    dv=pickle.load(f_inn)


# In[31]:


dv


# In[1]:


import xgboost as xg


# In[24]:


xg_model=xg.Booster()


# In[25]:


xg_model.load_model("model.json")


# In[26]:


xg_model


# In[38]:


#

# In[39]:
customeer={'journey_day': 'Sunday',
 'airline': 'Indigo',
 'class': 'Economy',
 'source': 'Bangalore',
 'departure': '6 AM - 12 PM',
 'total_stops': '1-stop',
 'arrival': '6 AM - 12 PM',
 'destination': 'Kolkata',
 'day_of_month': 19,
 'days_left': 35,
 'duration_in_hours': 5.6667}



app=Flask('airline')

@app.route('/deploy',methods=['post'])

def predict():
    #customeer=request.get_json()
    X=dv.transform([customeer])
    predd=xg_model.predict(xg.DMatrix(X))
    result={
        'Airline Ticket Price':float(predd)
    }
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)
# In[40]:


#X


# In[41]:


#predd=xg_model.predict(xg.DMatrix(X))


# In[42]:


#predd


# In[ ]:




