# MLZOOMCAM_MIDTERM_PROJECT

Airline Ticket Price Prediction

The project deals with the price prediction of airline ticket. The airline ticket prices depends on different paramters viz., class,source,destination,day of travel,time of travel. The ML model is trained based on different features viz., time of travel,ssource,destination,time of travel, month of travel,year of travel etc. 

Instructions:
 The dataset used for these project is https://www.kaggle.com/datasets/yashdharme36/airfare-ml-predicting-flight-fares.

 The data cleaning and preprocessing is done on the above dataset, and then exploratory data analysis is done and different ML regressions model viz. linear, tree based aand XG BOOST models and tested and it is followed by hyperparamter tuning. The final model chosen after hyperparmter tuning that tends to deliver with higher predction R2 and lower RMSE is XGBOOst model.

 The final model is loaded out in json format. Then it is converted in to a Flask application. Then it is dockerized as image and container. Then the model is deployed as webservice in Azure cloud.


 DATA Used : The dataset used for this project is Airline ticket price dataset obtained from the Kaggle website. The dataset can be downloaded from this link:

 https://www.kaggle.com/datasets/yashdharme36/airfare-ml-predicting-flight-fares
