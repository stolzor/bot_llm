from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "database"
    user: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    db_name: str = Field(alias="POSTGRES_DB")
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    database_url: str = "postgresql+asyncpg://{user}:{password}@{url}:5432/{db_name}"


def get_url() -> str:
    settings = Settings()
    db_url = settings.database_url.format(
        user="postgres",
        password=settings.password,
        db_name="postgres",
        url="172.18.0.3",
    )
    return db_url
