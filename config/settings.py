from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # CORS Configurations
    CORS_ALLOWED_ORIGINS: str
    CORS_ALLOWED_METHODS: str
    CORS_ALLOWED_HEADERS: str

    # APP Configurations
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool
    ENVIRONMENT: str

    # Logger Configurations
    LOGGER_NAME: str

    model_config = ConfigDict(env_file=".env")


app_settings = AppSettings()
