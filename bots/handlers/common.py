from aiogram.filters import Command
from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from .states import OrderMessage
from logger import get_logger


logger = get_logger(__name__, "bot.log")

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message, state: FSMContext):
    logger.info("User press command start")
    await state.clear()
    await message.answer(
        text="Go chating! :)", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(OrderMessage.stage_message_1)


@router.message(Command(commands=["end"]))
async def cmd_end(message: types.Message, state: FSMContext):
    logger.info("User press command end")
    await state.clear()
    await message.answer(text="Good bye!", reply_markup=types.ReplyKeyboardRemove())
