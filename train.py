from xgboost import XGBRegressor
from sklearn.feature_extraction import DictVectorizer
xgbmodel_hpt =  XGBRegressor(learning_rate=0.17,max_depth=15,min_child_weight=7)


xgbmodel_hpt.fit(x_train,y_train)

y_predxgbhpt=xgbmodel_hpt.predict(x_val)

print("R2 score is",r2_score(y_val,y_predxgbhpt))
# R2 score is 0.9591904202013563
print("Root mean squared error",np.sqrt(mean_squared_error(y_val,y_predxgbhpt)))
#Root mean squared error 4096.203891833892

'''Best Model

Based on the Analysis of different models viz., linear and tree based model with Hyperparamter tuning. 
The XG Boost regressor model delivered higher R2 score with lower Root mean squared error. 
The final model chosen for this project is XGB Regressor.'''

import pickle

with open('dvf.bin','wb') as f_out1:
  pickle.dump(dv,f_out1)

with open('modelf.sav','wb') as f_out3:
  pickle.dump(xgbmodel_hpt,f_out3)

