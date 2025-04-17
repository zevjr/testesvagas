from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.modules.calculator.usecase import router as router_calculate


def create_app():
    app = FastAPI(
        title="Car Insurance API",
        description="API for calculating car insurance premiums",
        version="1.0.0",
        default_response_class=JSONResponse
    )
    app.include_router(router_calculate)
    
    return app