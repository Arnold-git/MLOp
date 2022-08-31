from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from regression_model.config.core import config
from regression_model.processing.data_manager import load_dataset


from app.main import app

@pytest.fixture(scope="module")

