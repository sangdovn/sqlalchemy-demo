from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env"), env_file_encoding="utf-8")
    database_url: str = Field(validation_alias="DATABASE_URL")


settings = Settings()
