import math
from unittest import result

import numpy as np

from regression_model.predict import make_prediction


def test_make_prediction(sample_input_data):

    expected_first_prediction_value = 113422
    expected_no_predictions = 1449

    result = make_prediction(input_data=sample_input_data)

    predictions = result.get('predictions')
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert result.get('errors') is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)