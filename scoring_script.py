import xgboost as xg
import sklearn
import pickle
from sklearn.feature_extraction import DictVectorizer
import json
import flask
from flask import jsonify


from azureml.core import Model

dv = DictVectorizer(sparse=False)

input_file2='dvf.bin'

with open(input_file2,'rb') as f_inn:
    dv=pickle.load(f_inn)

dv


xg_model=xg.Booster()

def init():
    global model 
    model_name="airlineticketprice"
    path=Model.get_model_path(model_name)
    model=xg_model.load_model(path)

def run(data):
    try:
        data=json.loads(data)
        X=dv.transform([data])
        predd=model.predict(xg.DMatrix(X))
        result={
        'Airline Ticket Price':float(predd)}
        return jsonify(result)
    except Exception as er:
        error=str(er)
        return{'data':error,'message':'Failed to predict'}




