from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.token import TokenValidationError

from logger import get_logger

from .handlers import common, ordering_message
from .middlewares.spam import SpamMiddleware

logger = get_logger(__name__, "bot.log")


async def starter(token: str) -> Bot:
    redis_middleware = SpamMiddleware()
    storage = RedisStorage(redis=redis_middleware.client)
    dp = Dispatcher(storage=storage)
    dp.message.middleware.register(redis_middleware)

    logger.info("Enter token...")
    try:
        bot = Bot(token)
        logger.info("Insertion complete!")
    except TokenValidationError:
        logger.info("Token not valid")
        raise ValueError("Token not valid")

    dp.include_router(common.router)
    dp.include_router(ordering_message.router)

    await dp.start_polling(bot)
