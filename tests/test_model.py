import numpy as np
import pytest

from src.ml.model import train_model, compute_model_metrics, inference
from sklearn.linear_model import LogisticRegression


@pytest.fixture(scope="session")
def data():
    """Create dummy DataFrame."""
    X_train = np.array([[1, 2, 3], [4, 5, 6]])
    y_train = np.array([0, 1])
    return X_train, y_train


def test_train_model(data):
    """Test the train_model function."""
    # Create dummy data
    X, y = data

    # Train model
    model = train_model(X, y)

    # Check that the model is a LogisticRegression object
    assert isinstance(model, LogisticRegression)


def test_compute_model_metrics():
    """Test the compute_model_metrics function."""
    # Create dummy data
    y = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 1])
    preds = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 1])

    # Compute model metrics
    precision, recall, fbeta = compute_model_metrics(y, preds)

    # Check that the metrics are floats
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)


def test_inference(data):
    """Test the inference function."""
    # Create dummy data
    X, y = data

    # Create dummy model
    model = train_model(X, y)

    # Run inference
    preds = inference(model, X)

    # Check that the predictions are a numpy array
    assert isinstance(preds, np.ndarray)
