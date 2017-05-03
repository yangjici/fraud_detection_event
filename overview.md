# Fraud Detection Case Study - Group 3


## process flow

After some initial time in EDA, we split evenly model development amongst the team.  
This included identifying relationships between columns and hunches regarding potential relevancy.
Each team member took a stab at building a model, each a different one - the RandomForrestClassifier being the clear winner.  
Then came architecting to put the model in a pipeline, adding the flask front end with javascript, and a mondgo db.

The web app had to deal with two separate thread - one to run the web server and one to ping for new data points.  Rather than create a threading system, we opted to run each in its own python environment and sidetepped this.  

## preprocessing

We have a number of data cleaning steps to select a subset of colums.  This included imputing data, type conversions, and adding some new columns

### Final Model Predictor Variables:
1. gts
2. Event has organization description (engineered)
3. Where the event has organization name (engineered)
4. Whether the event has listed the address (engineered)
5. user age
6. user type
7. max ticket price
8. min ticket price
9. Total number of tickets the event are selling (engineered)
10. payout_type
11. number of previous payouts

## assessment metrics selected

Accuracy, precision, and recall

## validation and testing methodology

Standard model.fit, model.predict, and model.predict_proba

## parameter tuning involved in generating the model

GridSearchCV

## further steps you might have taken if you were to continue the project

Creating an ensemble of models.
