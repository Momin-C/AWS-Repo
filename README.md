# AWS-Repo
The Summer 2023 Mobile Health App team deployed one of the models and connected it to the iOS app, steps to replicate how this was done are listed below:

## Example Flask App Github (both have same files):
https://github.com/Momin-C/iOS_MHA
https://github.com/healthcaresystems-research-and-analysis/mha-model-deploy

## Google Docs Steps:
https://docs.google.com/document/d/1WNaXrGh7XWGT2ta2x0XBTsKM-Y1ukkF2sScnv_jtcoQ/edit?usp=sharing

## Requirements:
AWS Account

## Steps
1. Look into how the previous teams have created prediction ML models 
2. Export a prediction model to a tensorflow saved file
3. Create a Flask app that can handle requests to either process the sent data and then feed it into the model, or only feed data into the model (look at the example github aws_api.py or api.py files)
    This Flask app should import tensorflow and other necessary libraries
    In the same Github repository, there should be the saved file so that the Flask app can easily load up the model
4. Testing the Flask app:
    Change the “baseURL” in “PredictionManager.swift” to the URL that flask provides
    Start up the app, go to measurements (or on physician side, the patients tab then measurements) and go to the chart detail view for a patient that has 5+ recordings, see the “Predicted Value” bar and see if there is a value, if so move to step 5, otherwise fix the Flask app and PredictionManager (the example linked above should work on start-up)
5. Host model on AWS
    Follow this YouTube Videos steps (use t2.medium or t2.large since TF is a large library) Deploy ML on AWS EC2
    Change the link in the PredictionManager.swift and test again using steps in step 4

Improvements:
Look into using AWS Lambda instead since it’s free tier is higher and it charges based off requests instead of time run

