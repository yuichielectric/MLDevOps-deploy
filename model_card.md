# Model Card

## Model Details

The model analyzed in this card is a logistic regression model that predicts whether a person makes over 50K a year based on census data.

 - Person developing model: @yuichielectric
 - Model date: Jan 11th 2023
 - Model version: 1.0
 - Model Type: Logistic Regression
 - Framework: Scikit-learn
 - Version: 1.2.0
 - Language: Python 3.8.5

## Intended Use

This model is intended to be hosted as a RESTful API that can be used to predict whether a person makes over 50K a year based on census data.

## Training Data

The training data used to train this model is the census data from the UCI Machine Learning Repository. The data is available [here](https://archive.ics.uci.edu/ml/datasets/census+income).

## Evaluation Data

The test data used in the evaluation was a 20% split of the original census data. The rest of the 80% was used to train the model.

## Metrics

The model is evaluated using the following metrics:

 - Precision: 0.71
 - Recall: 0.62
 - F-beta Score: 0.66

## Ethical Considerations

 - The data may be biased in terms of race and sex.

## Caveats and Recommendations

 - The data used to train the model is from 1994. The model may not be as accurate for predicting income in 2023.
