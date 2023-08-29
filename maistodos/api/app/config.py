import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



class Settings(BaseSettings):
    environment: str = os.environ.get("ENVIRONMENT", "dev")
    service_name: str = "@maistodos/api"
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")

    class Config:
        env_file = ".env"


settings = Settings()
