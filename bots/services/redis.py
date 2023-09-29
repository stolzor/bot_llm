from aioredis import BlockingConnectionPool
from aioredis.client import Redis

from logger import get_logger

from ..settings import RedisConfig

logger = get_logger(__name__, "bot.log")


class RedisClient:
    def __init__(self, url: str | None = None, ex: int = 3) -> None:
        logger.info("Init Redis client")
        config = RedisConfig()
        if url is None:
            url = config.url

        self.ex = ex
        self.pool = BlockingConnectionPool.from_url(
            url,
            max_connections=int(config.connections),
            password=config.redis_password,
            port=config.redis_port,
        )
        self.client = Redis(connection_pool=self.pool)
