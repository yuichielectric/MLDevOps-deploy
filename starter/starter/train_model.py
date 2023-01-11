# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
from ml.data import process_data, load_csv
from ml.model import train_model, compute_model_metrics, inference, save_model

import os

# Add code to load in the data.
csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "census_cleaned.csv")
data = load_csv(csv_file_path)

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

columns_missing_values = [
    'workclass',
    'occupation',
    'native-country'
]

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True,
    columns_missing_values=columns_missing_values
)

# Proces the test data with the process_data function.
X_test, y_test, _, _ = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

# Train and save a model.
model = train_model(X_train, y_train)

precision, recall, fbeta = compute_model_metrics(y_test, inference(model, X_test))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("Fbeta: {:.2f}".format(fbeta))

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "model", "model.pkl")
encoder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "model", "encoder.pkl")
save_model(model, model_path)
save_model(encoder, encoder_path)
