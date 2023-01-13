import requests
import json

data = {
  "age": 0,
  "workclass": "Private",
  "fnlwgt": 0,
  "education": "Bachelors",
  "education-num": 0,
  "marital-status": "Married-civ-spouse",
  "occupation": "Tech-support",
  "relationship": "Wife",
  "race": "White",
  "sex": "Male",
  "capital-gain": 0,
  "capital-loss": 0,
  "hours-per-week": 0,
  "native-country": "United-States"
}

response = requests.post(
    'https://udacity-mldevope-engineer.herokuapp.com/predict',
    data=json.dumps(data)
    )

print(response.status_code)
print(response.json())
