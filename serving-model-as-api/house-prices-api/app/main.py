from typing import Any

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging


setup_app_logging(config=settings)


def customise_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(

        title = "House Price prediction API",
        version = "1.0",
        description = "House Price Prediction API by ArnoldIG",
        routes = app.routes,
        )

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

root_router = APIRouter()

@root_router.get("/")
def index(request: Request) -> Any:
    """
    Basic HTML response
    """
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to House Price Prediction API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)
customise_openapi(app)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if __name__ == "__main__":
    logger.warning("Running server in development mode")
    import uvicorn 

    uvicorn.run(
    app, host="localhost",
    port=8001,
    log_level="debug"
    )