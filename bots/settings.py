import os

from dotenv import load_dotenv


load_dotenv()


class RedisConfig:
    redis_password = os.getenv("REDIS_PASSWORD")
    redis_port = os.getenv("REDIS_PORT")
    connections = os.getenv("REDIS_CONNECTION")
    url = os.getenv("REDIS_URL")
