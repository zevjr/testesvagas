from app.config import settings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import logging
import logging.config
from app.routes import api_router_v1

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title=settings.service_name, root_path="/checkout")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(api_router_v1, prefix='/ap1/v1')

    logger.info(f"starting app {settings.service_name}")

    return app
