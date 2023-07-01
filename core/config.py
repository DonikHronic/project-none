import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

from core.responses import default_error_response

load_dotenv()


class Settings(BaseSettings):
    """Base project settings"""

    PROJECT_NAME: str = "Super project"
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    HOST: str = os.getenv("PROJECT_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PROJECT_PORT", 8000))

    # postgres
    PG_HOST: str = os.getenv("PG_HOST", "localhost")
    PG_PORT: int = int(os.getenv("PG_PORT", 5432))
    PG_USER: str = os.getenv("PG_USER", "postgres")
    PG_PASSWORD: str = os.getenv("PG_PASSWORD", "postgres")
    PG_DB: str = os.getenv("PG_DB", "postgres")

    # redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB: int = int(os.getenv("REDIS_DB", 0))
    REDIS_USER: str = os.getenv("REDIS_USER", "redis")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "redis")

    # logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # apps
    APPS = ["core", "user", "post"]

    # validation
    VALIDATION_ERROR_RESPONSE: dict = {
        "400": {
            "description": "Error",
            "content": {"application/json": {"examples": {"Error": {"value": default_error_response.dict()}}}},
        },
        "422": {
            "description": "RequestValidationError",
            "content": {"application/json": {"examples": {"Error": {"value": default_error_response.dict()}}}},
        },
    }


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
