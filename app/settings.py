"""Application settings."""
import os

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    """Application settings class."""

    telegram_token: str


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),  # type: ignore
)
