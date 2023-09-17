from typing import Any, Callable, Dict, Awaitable

from aioredis import BlockingConnectionPool
from aioredis.client import Redis
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from ..settings import RedisConfig
from logger import get_logger


logger = get_logger(__name__, "bot.log")


class RedisMiddleware(BaseMiddleware):
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

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user_id = f"user_{event.from_user.id}"

        check_user = await self.client.get(name=user_id)

        if check_user:
            if int(check_user.decode()) == 1:
                await self.client.set(name=user_id, value=0, ex=self.ex)
                return await event.answer("Wait please I'm not that fast ;)")
            return
        await self.client.set(name=user_id, value=1, ex=self.ex)

        return await handler(event, data)


if __name__ == "__main__":
    redis_middleware = RedisMiddleware("redis://localhost")
