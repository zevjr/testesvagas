import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    environment: str = os.environ.get("ENVIRONMENT", "dev")
    service_name: str = "@maistodos/api"
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
    is_sqlite: bool = bool(os.environ.get("IS_SQLITE", True))

    database_url: str = (
        "sqlite:///db.db" if is_sqlite else os.environ.get("DATABASE_URL", "")
    )


settings = Settings()
