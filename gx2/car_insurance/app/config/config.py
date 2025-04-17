from pydantic_settings import BaseSettings
import os

def get_env(key: str, default: str, is_int: bool = False) -> str:
    if os.getenv(key) and not is_int:
        return os.getenv(key)
    elif os.getenv(key) and is_int:
        return int(os.getenv(key))
    else:
        return default

class Settings(BaseSettings):
    COVERAGE_PERCENTAGE: float = get_env("COVERAGE_PERCENTAGE", 1.0, True)
    AGE_RATE_INCREMENT: float = get_env("AGE_RATE_INCREMENT", 0.005, True)
    VALUE_RATE_INCREMENT: float = get_env("VALUE_RATE_INCREMENT", 0.005, True)
    VALUE_INCREMENT_STEP: int = get_env("VALUE_INCREMENT_STEP", 10000, True)
    MIN_GIS_ADJUSTMENT: float = get_env("MIN_GIS_ADJUSTMENT", -0.02, True)
    MAX_GIS_ADJUSTMENT: float = get_env("MAX_GIS_ADJUSTMENT", 0.02, True)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()