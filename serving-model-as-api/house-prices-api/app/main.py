import logging
import sys
from types import FrameType 
from typing import List, cast

from loguru import logger
from pydantic import AnyHttpUrl, BaseSettings

class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    logging: LoggingSettings = LoggingSettings()

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://localhost:3000",
        "https://localhost:8000"
    ]

    PROJECT_NAME: str = "House Price Prediction API"

    class Config: 
        case_sensitive = True