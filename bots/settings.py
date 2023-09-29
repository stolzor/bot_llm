import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class RedisConfig(BaseSettings):
    redis_password: str = os.getenv("REDIS_PASSWORD")
    redis_port: str = os.getenv("REDIS_PORT")
    connections: str = os.getenv("REDIS_CONNECTION")
    url: str = os.getenv("REDIS_URL")
