from typing import Dict, Awaitable, Callable, Any

from aiogram.types import TelegramObject, Message

from .redis import RedisMiddleware
from logger import get_logger


logger = get_logger(__name__, "bot.log")


class SpamMiddleware(RedisMiddleware):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        logger.info("Init Spam middleware")

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
                await self.client.set(name=user_id, value=0, ex=10)
                return await event.answer("Wait please I'm not that fast ;)")
            return
        await self.client.set(name=user_id, value=1, ex=10)

        return await handler(event, data)
