import asyncio
import os

from dotenv import load_dotenv

from bots.start import starter
from logger import get_logger


load_dotenv()
logger = get_logger(__name__, "bot.log")


if __name__ == "__main__":
    logger.info("Start bot")
    asyncio.run(starter(os.getenv("TOKEN")))
