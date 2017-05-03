# Fraud Detection Case Study - Group 3


## process flow

After some initial time in EDA, we split evenly model development amongst the team.  
This included identifying relationships between columns and hunches regarding potential relevancy.
Each took a stab at building a model, each a different one - the RandomForrestClassifier being the clear winner.  
Then came architecting to put the model in a pipeline, adding the flask front end with javascript, and a mondgo db.

## preprocessing

We have a number of data cleaning steps to select a subset of colums.  This included imputing data, type conversions, and adding some new columns

## assessment metrics selected

Accuracy, precision, and recall

## validation and testing methodology

Standard model.fit, model.predict, and model.predict_proba

## parameter tuning involved in generating the model

GridSearchCV

## further steps you might have taken if you were to continue the project

Creating an ensemble of models.
