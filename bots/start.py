from aiogram import Bot, Dispatcher
from aiogram.utils.token import TokenValidationError

from .middlewares.spam import SpamMiddleware
from .handlers import common, ordering_message
from logger import get_logger


logger = get_logger(__name__, "bot.log")


async def starter(token: str) -> Bot:
    redis_middleware = SpamMiddleware()
    dp = Dispatcher()
    dp.message.middleware.register(redis_middleware)

    logger.info("Enter token...")
    try:
        bot = Bot(token)
    except TokenValidationError:
        raise ValueError("Token not valid")

    dp.include_router(common.router)
    dp.include_router(ordering_message.router)

    await dp.start_polling(bot)
