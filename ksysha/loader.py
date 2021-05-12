from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_API = '1741325585:AAFdGXNSDIwT3Qc3uTT3zCQgpkWLU9OAYTE'

storage = MemoryStorage()
bot = Bot(BOT_API)
dp = Dispatcher(bot, storage=storage)
