from aiogram import types
from loader import dp, bot
from states import Story
from .sql import update
from aiogram.dispatcher.filters import Text


keyboard_start = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_start.add(types.KeyboardButton('дальше'),
                   types.KeyboardButton('информация'))

# каждый раз копировать и заменять имя кейборд
# вот types нужно добавлять если есть еще варианты
keyboard_1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_1.add(types.KeyboardButton('да'),
               types.KeyboardButton('нет'),
               types.KeyboardButton('информация'))


async def start_story(message: types.Message):
    print(message.from_user.id)
    data = update(message.from_user.id)


    text = f"""Привет {data[1]}!\n
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

think = 'Кажется, надо хорошенько обдумать план действий. Реши головоломку, чтобы придумать, что делать.\n' + '#' * 50
wrans = 'Неверный ответ. Попробуй ещё раз.'
death = 0
glade, thicket = 0, 0
lake, hills = 0, 0
left, right = 0, 0
drg = 0
grap = 0
# вот это короче надо копировать для каждого этапа, заменять свои
@dp.message_handler(state=Story.state_1)
async def state_1(message: types.Message):

    if message.text == 'дальше':
        #update(message.from_user.id, apples=2)
        # следующий этап указать свою клавиатуру
        # await bot.send_photo(message.chat.id, open('assets\\1.png'))
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

@dp.message_handler(state=Story.state_2)
async def state_2(message: types.Message):

    if message.text == 'да':
        #update(message.from_user.id, apples=2)
        # следующий этап указать свою клавиатуру
        # await bot.send_photo(message.chat.id, open('assets\\1.png'))
        await message.answer(f"""
        Ты начинаешь копать...\n
        \tПри совершении некоторых действий придётся хорошо подумать. Иногда это довольно сложно,\n
        будто ты решаешь настоящую головоломку. Режим решения головоломки выделяется "#".\n\n', {think}
        Правильный ответ на любую головоломку содержит одно слово или одно число. Числа нужно вводить цифрами)\n
        Сколько лап у кота?\n
        """, reply_markup=keyboard_1)
        await Story.state_3.set()

    elif message.text == 'нет':
        await message.answer(f"""
                Прости, что лишаю тебя выбора, но раскопка является частью обучения.\n
                Ты начинаешь копать...\n
                \tПри совершении некоторых действий придётся хорошо подумать. Иногда это довольно сложно,\n
                будто ты решаешь настоящую головоломку. Режим решения головоломки выделяется "#".\n\n', {think}
                Правильный ответ на любую головоломку содержит одно слово или одно число. Числа нужно вводить цифрами)\n
                Сколько лап у кота?\n
                """, reply_markup=keyboard_1)
        await Story.state_3.set()
    elif message.text == 'информация':
        await info(message)

    #else:
        #неверно
        #update(message.from_user.id, health=-2)
        #await message.answer('State_2_text', reply_markup=keyboard_1)
        #await Story.state_2.set()