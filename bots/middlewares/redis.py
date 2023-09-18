from abc import ABC
from typing import Any

from aioredis import BlockingConnectionPool
from aioredis.client import Redis
from aiogram import BaseMiddleware

from ..settings import RedisConfig
from logger import get_logger


logger = get_logger(__name__, "bot.log")


class RedisMiddleware(BaseMiddleware, ABC):
    """Middleware for cache session user."""

    def __init__(self, url: str = None, ex: int = 3) -> None:
        logger.info("Init Redis middleware")
        if url is None:
            url = RedisConfig.url

        self.ex = ex
        self.pool = BlockingConnectionPool.from_url(
            url,
            max_connections=int(RedisConfig.connections),
            password=RedisConfig.redis_password,
            port=RedisConfig.redis_port,
        )
        self.client = Redis(connection_pool=self.pool)

    async def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError()


if __name__ == "__main__":
    redis_middleware = RedisMiddleware("redis://localhost")
