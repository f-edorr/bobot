from aiogram.dispatcher.filters.state import StatesGroup, State


class Main(StatesGroup):
    start_name = State()
    start_gender = State()
