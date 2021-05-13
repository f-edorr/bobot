from aiogram import types
from telegram_bot.loader import dp, bot
from telegram_bot.states import Story
from telegram_bot.handlers.sql import update
from aiogram.dispatcher.filters import Text


keyboard_start = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_start.add(types.KeyboardButton('дальше'),
                   types.KeyboardButton('информация'))

keyboard_1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_1.add(types.KeyboardButton('да'),
               types.KeyboardButton('нет'),
               types.KeyboardButton('информация'))

keyboard_2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_2.add(types.KeyboardButton('25'),
               types.KeyboardButton('4'),
               types.KeyboardButton('информация'))

keyboard_3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_3.add(types.KeyboardButton('чаща'),
               types.KeyboardButton('поляна'),
               types.KeyboardButton('информация'))

keyboard_4 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_4.add(types.KeyboardButton('тромбоциты'),
               types.KeyboardButton('эритроциты'),
               types.KeyboardButton('информация'))


async def start_story(message: types.Message):
    print(message.from_user.id)
    data = update(message.from_user.id)


    text = f"""Привет {data[2]}!\n
            \tТы, наверное, ничего не помнишь. Давай я всё объясню.\n
            Ты - любознательный исследователь, изучающий мир. Не так давно ты забрёл в бескрайний лес,\n
            и не смог выбраться. Это место, полное загадок, очаровало тебя, и ты заходил всё дальше и дальше, пока\n
            окончательно не заблудился.\n
            По пути тебе встретился монстр. Он подкрался сзади и ударил тебя по голове, забрал все твои вещи и исчез.\n
            Судя по тому, что ты потерял память, монстр был силён. Будем надеятся, ты не встретишь его снова.\n\n
            \tВ этом лесу происходят странные вещи, жизнь здесь проходит несколько по другим правилам.\n
            Например, у каждого существа, включая тебя, есть свой LV. Чем больше твой LV,\n
            тем больше у тебя возможностей. Чтобы повысить его, нужно решать головоломки и сражаться с мострами.\n
            Также у тебя есть HP. Это показатель твоего здоровья. Когда HP станет равным нулю, тебе придётся есть яблоки.\n
            Если у тебя нет яблок, придётся их купить. 1 яблоко == 20 HP == 20 монеток.\n
            Если твой HP равен нулю, яблок нет и монеток тоже, ты умрёшь. Твой путь на этом закончится, и прогресс\n
            будет потерян. Игра завершится.\n\n
            \tХочешь найти свои украденные вещи? Хорошо, давай отправляться в путь.\n
            Осторожно, ночью здесь очень темно.\n
        """
    #if data[2] == 1:
    #    await bot.send_photo(message.chat.id, open('images\\main_male_.png'))
    #else:
    #    await bot.send_photo(message.chat.id, open('images\\main_fem_.png'))
    await message.answer(text, reply_markup=keyboard_start)
    await Story.state_1.set()


# информация
async def info(message: types.Message):
    """
    param user_id: 0
    param name: 1
    param gender:
    param apples:
    param moneys:
    param health:
    param level:
    param inventory:
    param weapon:

    """
    data = update(message.from_user.id)
    await message.answer(f"""
HP: {data[5]}, LV: {data[6]}, Кол-во яблок: {data[3]}, Кол-во монеток: {data[5]}\n
Оружие: {data[8]}\n
Инвентарь: {data[7]}\n
""")

think = 'Кажется, надо хорошенько обдумать план действий. Реши головоломку, чтобы придумать, что делать.\n'
wrans = 'Неверный ответ. Попробуй ещё раз.\nТебя атакуют! Ты теряешь 10 HP!\n'
death = 0
glade, thicket = 0, 0
lake, hills = 0, 0
left, right = 0, 0
drg = 0
grap = 0

# яма
@dp.message_handler(state=Story.state_1)
async def state_1(message: types.Message):

    if message.text == 'дальше':
        #update(message.from_user.id, apples=2)
        # await bot.send_photo(message.chat.id, open('images\\treasure_.png'))
        await message.answer(f"""Отлично! Я знал, что ты справишься!\n
                  \tТы шёл, разглядывая кусты вокруг. На них растёт множество ягод!\n
                  ...Кажется, они не съедобны. Пока всё же лучше держаться на яблоках.\n
                  Погоди-ка! Под одним из кустов ты обнаружил нечто странное. Похоже, там что-то закопано.\n
                  Раскопать?""", reply_markup=keyboard_1)
        await Story.state_2.set()

    elif message.text == 'информация':
        await info(message)

    #else:
        #неверно
        #update(message.from_user.id, health=-2)
        #await message.answer('State_2_text', reply_markup=keyboard_1)
        #await Story.state_2.set()

#раскопка
@dp.message_handler(state=Story.state_2)
async def state_2(message: types.Message):

    if message.text == 'да':
        # update(message.from_user.id, apples=2)
        # await bot.send_photo(message.chat.id, open('assets\\1.png'))
        await message.answer(f"""
        Ты начинаешь копать...\n
        \tПри совершении некоторых действий придётся хорошо подумать. Иногда это довольно сложно,\n
        будто ты решаешь настоящую головоломку.\n\n {think}\n
        Сколько лап у кота?\n
        """, reply_markup=keyboard_2)
        await Story.state_3.set()

    elif message.text == 'нет':
        await message.answer(f"""
                Прости, что лишаю тебя выбора, но раскопка является частью обучения.\n
                Ты начинаешь копать...\n
                \tПри совершении некоторых действий придётся хорошо подумать. Иногда это довольно сложно,\n
                будто ты решаешь настоящую головоломку.\n\n {think}
                Сколько лап у кота?\n
                """, reply_markup=keyboard_2)
        await Story.state_3.set()
    elif message.text == 'информация':
        await info(message)

#сколько лап у кота
@dp.message_handler(state=Story.state_3)
async def state_3(message: types.Message):

    if message.text == '4':
        #update(message.from_user.id, apples=2)
        # await bot.send_photo(message.chat.id, open('images\\treasure_.png'))
        await message.answer(f"""Верно!\n
        Ты получил: монетки х100, яблоки х1, деревянный меч\nТвой LV повысился!\n
        \tПоздравляю, ты научился решать головоломки!\n
        Ты откопал меч, яблоко и монетки! Теперь ты готов ко всему.\n
        \tТы продолжил идти вперёд.\n
        Ты добрался до большого старого дуба, словно из сказки. Дальше ты можешь пойти\n
        на маленькую полянку, или в густую чащу. Куда направишься?\n
        """, reply_markup=keyboard_3)
        update(message.from_user.id, moneys=100)
        update(message.from_user.id, apples=1)
        update(message.from_user.id, weapon='деревянный меч')
        update(message.from_user.id, level=1)
        await Story.state_4.set()

    elif message.text == 'информация':
        await info(message)

    elif message.text == '25':
        await message.answer(wrans, reply_markup=keyboard_2)

#поляна или чаща
@dp.message_handler(state=Story.state_4)
async def state_4(message: types.Message):

    if message.text == 'чаща':
        #update(message.from_user.id, apples=2)
        #await bot.send_photo(message.chat.id, open('images\\bear.png'))
        thicket = 1
        await message.answer(f"""\tТы направился в густую чащу. Здесь темно, но путь освещает множество светлячков...\n
        Вокруг деревьев и кустов распустились сказочные цветы. Стой, не срывай их! Пусть цветут дальше!\n
        ...Что это, там, впереди? Кажется, это монстр!\n
        Он выглядит как маленький медвежонок с рогами. Он такой милый! UwU\n
        Секунду... Он пытается тебя убить!\n\n
        \tЧтобы атаковать монстра, нужна верная тактика.\n {think}
        """, reply_markup=keyboard_4)
        await Story.state_5.set()

    elif message.text == 'информация':
        await info(message)

    elif message.text == 'поляна':
        glade = 1
        # await bot.send_photo(message.chat.id, open('images\\bear.png'))
        await message.answer(f"""\tТы направился к маленькой полянке. Здесь так тихо и красиво...\n
                Нежные звуки сверчков манят уснуть... Эй! Не поддавайся!\n
                ...Что это, там, впереди? Кажется, это монстр!\n
                Он выглядит как маленький медвежонок с рогами. Он такой милый! UwU\n
                Секунду... Он пытается тебя убить!\n\n
                \tЧтобы атаковать монстра, нужна верная тактика.\n{think}
                """, reply_markup=keyboard_4)
        await Story.state_5.set()

#медвежонок
@dp.message_handler(state=Story.state_5)
async def state_5(message: types.Message):

    if message.text == 'тромбоциты':
        update(message.from_user.id, apples=2)
        if thicket:
            await message.answer(f"""Верно!\n
            Ты получил: монетки х200, яблоки х1, ромашка х1\n
            Твой LV повысился!\n
            Отдышавшись после битвы, ты заходишь всё дальше в лес...\n
            """, reply_markup=keyboard_3)
            update(message.from_user.id, moneys=200)
            update(message.from_user.id, apples=1)
            update(message.from_user.id, inventory=', ромашка')
            update(message.from_user.id, level=1)
        if glade:
            await message.answer(f"""Верно!\n
            Ты получил: монетки х100, яблоки х1, лилия х1\n
            Прогулявшись по полянке, ты заходишь всё дальше в лес...\n
            """, reply_markup=keyboard_3)
            update(message.from_user.id, moneys=100)
            update(message.from_user.id, apples=1)
            update(message.from_user.id, inventory=', лилия')
        await Story.state_6.set()

    elif message.text == 'информация':
        await info(message)

    elif message.text == 'эритроциты':
        update(message.from_user.id, health=-10)
        await message.answer(wrans, reply_markup=keyboard_2)

#забавный монстр
@dp.message_handler(state=Story.state_5)
async def state_5(message: types.Message):

    if message.text == 'тромбоциты':
        update(message.from_user.id, apples=2)
        if thicket:
            await message.answer(f"""Верно!\n
            Ты получил: монетки х200, яблоки х1, ромашка х1\n
            Твой LV повысился!\n
            Отдышавшись после битвы, ты заходишь всё дальше в лес...\n
            """, reply_markup=keyboard_3)
            update(message.from_user.id, moneys=200)
            update(message.from_user.id, apples=1)
            update(message.from_user.id, inventory=', ромашка')
            update(message.from_user.id, level=1)
        if glade:
            await message.answer(f"""Верно!\n
            Ты получил: монетки х100, яблоки х1, лилия х1\n
            Прогулявшись по полянке, ты заходишь всё дальше в лес...\n
            """, reply_markup=keyboard_3)
            update(message.from_user.id, moneys=100)
            update(message.from_user.id, apples=1)
            update(message.from_user.id, inventory=', лилия')
        await Story.state_6.set()

    elif message.text == 'информация':
        await info(message)

    elif message.text == 'эритроциты':
        update(message.from_user.id, health=-10)
        await message.answer(wrans, reply_markup=keyboard_2)