import imp
import json
from sys import api_version
from typing import Any

import numpy as np
import pandas as pd 
from fastapi import APIRouter, HTTPException 
from fastapi.encoders import jsonable_encoder 
from loguru import logger 
from regression_model import __version__ as model_version 
from regression_model.predict import make_prediction 


from app import __version__, schemas
from app.config import Settings

api_router  =APIRouter()

@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=Settings.PROJECT_NAME, api_version =__version__, model_version=model_version
    )
    return health.dict()

@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def  predict(input_data: schemas.MultipleHouseDataInputs) -> Any:

    """
    Prediction with arnold-house-price-regression-model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.input))

    logger.info(f"Making prediction on inputs: {input_data.input}")
    results = make_prediction(input_data=input_df.replace({ np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))
    logger.info(f"Prediction results: {results.get('predictions')}")
