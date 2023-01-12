# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
from ml.data import process_data, load_csv
from ml.model import train_model, compute_model_metrics, inference, save_model
from constants import CATEGORICAL_FEATURES, COLUMNS_MISSING_VALUES

import os

# Add code to load in the data.
dirname = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(dirname, "..", "data", "census_cleaned.csv")
data = load_csv(csv_file_path)

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=CATEGORICAL_FEATURES, label="salary", training=True,
    columns_missing_values=COLUMNS_MISSING_VALUES
)

# Proces the test data with the process_data function.
X_test, y_test, _, _ = process_data(
    test, categorical_features=CATEGORICAL_FEATURES, label="salary", training=False, encoder=encoder, lb=lb,
    columns_missing_values=COLUMNS_MISSING_VALUES
)

# Train and save a model.
model = train_model(X_train, y_train)

precision, recall, fbeta = compute_model_metrics(y_test, inference(model, X_test))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("Fbeta: {:.2f}".format(fbeta))

model_path = os.path.join(dirname, "..", "model", "model.pkl")
encoder_path = os.path.join(dirname, "..", "model", "encoder.pkl")
lb_path = os.path.join(dirname, "..", "model", "lb.pkl")
save_model(model, model_path)
save_model(encoder, encoder_path)
save_model(lb, lb_path)

# Compute the slice performance metrics for education column.
with open(os.path.join(dirname, "education_slice_performance.txt"), "w") as f:
    f.write("# Slice performance metrics for education column" + os.linesep + os.linesep)
    for slice in data["education"].unique():
        X_slice, y_slice, _, _ = process_data(
            data[data["education"] == slice], categorical_features=CATEGORICAL_FEATURES, label="salary", training=False, encoder=encoder, lb=lb
        )
        precision, recall, fbeta = compute_model_metrics(y_slice, inference(model, X_slice))

        f.write('Slice {:13s}: precision: {:.2f}, recall: {:.2f}, Fbeta: {:.2f}'.format(slice, precision, recall, fbeta))
        f.write(os.linesep)
