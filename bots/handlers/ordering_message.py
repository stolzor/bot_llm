from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from .states import OrderMessage
from logger import get_logger


logger = get_logger(__name__, "bot.log")

router = Router()


@router.message(OrderMessage.stage_message_1)
async def greeting(message: types.Message, state: FSMContext):
    await message.answer("YO")
