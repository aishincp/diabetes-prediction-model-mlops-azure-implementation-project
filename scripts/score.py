import joblib
import json
import numpy as np
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path(model_name='diabetes-lr')
    model = joblib.load(model_path)

def run(raw_data):
    data = np.array(json.loads(raw_data)['data'])
    result = model.predict(data)
    return json.dumps({"prediction": result.tolist()})