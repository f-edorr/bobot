from pathlib import Path
from aiogram import types
from telegram_bot.loader import dp
from telegram_bot.states import Main
from aiogram.dispatcher import FSMContext
import sqlite3 as sql
from .main import start_story

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB = BASE_DIR/'db.sqlite3'

keyboard = types.InlineKeyboardMarkup()
keyboard.row(types.InlineKeyboardButton('🚹 Мужской', callback_data='1'),
             types.InlineKeyboardButton('🚺 Женский', callback_data='0'))


@dp.message_handler(commands='start')
async def start(message: types.Message):

    await message.answer('Введи имя')
    await Main.start_name.set()


@dp.message_handler(state=Main.start_name)
async def name(message: types.Message, state: FSMContext):
    await message.answer(f'Привет, {message.text}, введите пол персонажа', reply_markup=keyboard)
    await state.update_data({
        'name': message.text,
    })
    await Main.start_gender.set()


@dp.callback_query_handler(state=Main.start_gender)
async def gender(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({
        'gender': int(call.data),
    })
    data = await state.get_data()
    data = (None, call.message.from_user.id, data['name'], data['gender'], 0, 0, 0, 0, '', '')
    with sql.connect(DB) as conn:
        cur = conn.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS '
        #            'users(id INTEGER PRIMARY KEY, user_id INT, name TEXT, gender BOOL, apples INT, moneys INT, '
        #             'health INT, level INT, inventory TEXT, weapon TEXT)')
        #conn.commit()

        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", data)
        conn.commit()
        cur.close()
    await start_story(message=call.message)
