from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "database"
    user: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    db_name: str = Field(alias="POSTGRES_DB")
    model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra="allow")
    database_url: str = "postgresql+asyncpg://{user}:{password}@localhost:5432/{db_name}"
