from aiogram.fsm.state import StatesGroup, State


class OrderMessage(StatesGroup):
    stage_message_1 = State()
    stage_message_2 = State()
    stage_message_3 = State()
