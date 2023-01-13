from fastapi import FastAPI
from request_model import Input
from starter.constants import CATEGORICAL_FEATURES, COLUMNS_MISSING_VALUES

import os
import pandas as pd

from starter.ml.model import inference, load_model
from starter.ml.data import process_data


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")


app = FastAPI()

dirname = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(dirname, "model/model.pkl"))
encoder = load_model(os.path.join(dirname, "model/encoder.pkl"))
lb = load_model(os.path.join(dirname, "model/lb.pkl"))

@app.get("/")
async def root():
    return {"message": "Welcome to the model inference API!"}


@app.post("/predict")
async def predict(input: Input):
    input_data = pd.DataFrame.from_dict([input.dict(by_alias=True)])
    input_data, _, _, _ = process_data(
        input_data, categorical_features=CATEGORICAL_FEATURES,
        columns_missing_values=COLUMNS_MISSING_VALUES,
        training=False, encoder=encoder, lb=lb)
    prediction = ">50K" if inference(model, input_data) == 1 else "<=50K"
    return {"prediction": prediction}
