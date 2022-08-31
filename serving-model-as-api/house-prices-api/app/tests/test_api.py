import math

import numpy as np 
import pandas as pd 
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:

    payload = {
        "inputs": test_data.replace({
            np.nan: None
        }).to_dict(orient="records")
    }

    response = client.post(
        "http://localhost:8000/api/v1/predict",
        json=payload
    )

    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["prediction"]
    assert prediction_data["errors"] is None 
    assert math.isclose(prediction_data["prediction"][0], 113422, rel_tol=100)