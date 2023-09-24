import os

from pydantic import Field

from ...settings.base import AdvancedBaseSettings


class ServiceDatabaseSettings(AdvancedBaseSettings):
    """
    Child class which consist attributes for connect to postgresql

    Attributes:

    """

    host: str = Field(default="localhost")
    user: str = Field(default="postgres")
    port: int = Field(default=5432)
    db_name: str = Field(default="postgres")
    password: str

    class Config:
        env_prefix = "POSTGRES_"
        env_dir = os.path.join(AdvancedBaseSettings.get_dir(), "..", "database", "env")
        print(env_dir)

    @property
    def postgresql_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:5432/{self.db_name}"


if __name__ == "__main__":
    settings = ServiceDatabaseSettings()
    print(settings.postgresql_url)
