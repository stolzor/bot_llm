import os

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from ...settings.base import AdvancedBaseSettings


class ServiceDatabaseSettings(AdvancedBaseSettings):
    """
    Child class which consist attributes for connect to postgresql

    Attributes:
        host (str): host database
        user (str): username database
        port (str): port database
        db (str): database name
        password (str): password database

    """

    host: str = Field(default="localhost")
    user: str = Field(default="postgres")
    port: str = Field(..., env="POSTGRES_PORT")
    db: str = Field(default="postgres")
    password: str

    path_dir: str = os.path.join(
        AdvancedBaseSettings.get_dir(), "..", "database", "env", ".env"
    )
    model_config = SettingsConfigDict(env_file=path_dir, env_prefix="POSTGRES_")

    @property
    def postgresql_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


if __name__ == "__main__":
    settings = ServiceDatabaseSettings()
    print(settings.postgresql_url)
