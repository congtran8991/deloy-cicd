from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    APP_NAME: str = Field(default="FastAPI App")
    APP_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)

    # Database
    DATABASE_URL: str = Field(default="sqlite:///./app.db")

    # Security
    SECRET_KEY: str = Field(default="change-this-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
    }


settings = Settings()
