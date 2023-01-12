from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the model inference API!"}

def test_predict_without_input():
    response = client.post("/predict")
    assert response.status_code == 422

def test_predict_for_salary_under_50k():
    input = {
        "age": 39,
        "workclass": "State-gov",
        "fnlwgt": 77516,
        "education": "Bachelors",
        "education-num": 13,
        "marital-status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital-gain": 2174,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "United-States"
    }
    response = client.post("/predict", json=input)
    assert response.status_code == 200
    assert response.json() == {"prediction": "<=50K"}

def test_predict_for_salary_over_50k():
    input = {
        "age": 37,
        "workclass": "Private",
        "fnlwgt": 280464,
        "education": "Some-college",
        "education-num": 10,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 80,
        "native-country": "United-States"
    }
    response = client.post("/predict", json=input)
    print(response)
    assert response.status_code == 200
    assert response.json() == {"prediction": ">50K"}
