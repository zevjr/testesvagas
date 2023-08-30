import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    environment: str = os.environ.get("ENVIRONMENT", "dev")
    service_name: str = "@maistodos/api"
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")


settings = Settings()
