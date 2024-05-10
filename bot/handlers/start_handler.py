import json
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove

from bot.buttons.inline_buttons import language_buttons
from bot.buttons.reply_buttons import start_menu_buttons, back_main_menu_button, main_menu_buttons
from bot.buttons.text import sign_in, back_main_menu, sign_up, sign_in_ru, log_out, sign_up_ru, log_out_ru, \
    back_main_menu_ru, choice_language, choice_language_ru
from bot.dispatcher import dp, bot
from main import admins


def validate_phone_number(phone_number):
    if len(phone_number) == 13 and phone_number[:4] == "+998":
        return True
    return False


@dp.message_handler(Text(equals=[back_main_menu, back_main_menu_ru]))
async def back_main_menu_function_1(msg: types.Message):
    await msg.answer(text=f"""
/start buyrug'ini yuboring ❗

----------------------------

Отправьте команду /start ❗""", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=[back_main_menu, back_main_menu_ru]), state=['sign_in_1', 'sign_in_2', 'sign_up_1'])
async def back_main_menu_function_1(msg: types.Message, state: FSMContext):
    if msg.text == back_main_menu:
        await msg.answer(text=f"Asosiy menu🏠", reply_markup=await start_menu_buttons(msg.from_user.id))
    else:
        await msg.answer(text=f"Главное меню🏠", reply_markup=await start_menu_buttons(msg.from_user.id))
    await state.finish()


@dp.message_handler(Text(equals=[back_main_menu, back_main_menu_ru]),
                    state=['test_performance_1', 'test_performance_2'])
async def back_main_menu_function_1(msg: types.Message, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            if msg.text == back_main_menu:
                await msg.answer(text="Avval kirish bosqichini amalga oshiring ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
            else:
                await msg.answer(text="Сначала выполните вход в систему ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
    except KeyError:
        if msg.text == back_main_menu:
            await msg.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer(text=f"Главное меню🏠", reply_markup=await start_menu_buttons(msg.from_user.id))
        await state.finish()


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            await state.set_state('language_1')
            await msg.answer(text="""
Tilni tanlang

-------------

Выберите язык""", reply_markup=await language_buttons())
    except KeyError:
        if tg_user['language'] == 'uz':
            await msg.answer(text="Bot yangilandi ♻️", reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer(text="Бот обновлен ♻️", reply_markup=await main_menu_buttons(msg.from_user.id))
    try:
        if tg_user['detail']:
            for admin in admins:
                await bot.send_message(chat_id=admin, text=f"""
Yangi user🆕
ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>
Ism-Familiya: {msg.from_user.full_name}
Username: @{msg.from_user.username}\n""", parse_mode='HTML')
            data = {
                "chat_id": str(msg.from_user.id),
                "username": msg.from_user.username,
                "full_name": msg.from_user.full_name,
                "language": 'uz'
            }
            requests.post(url=f"http://127.0.0.1:8000/telegram-users/create/", data=data)
    except KeyError:
        pass


@dp.callback_query_handler(Text(startswith='language_'), state='language_1')
async def language_function_1(call: types.CallbackQuery, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    data = {
        "chat_id": str(call.from_user.id),
        "username": call.from_user.username,
        "full_name": call.from_user.full_name,
        "language": call.data.split("_")[-1]
    }
    requests.put(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data)
    await call.message.delete()
    if call.data.split("_")[-1] == 'uz':
        await call.message.answer(text="Infinity Academy botiga hush kelibsiz ☺",
                                  reply_markup=await start_menu_buttons(call.from_user.id))
    else:
        await call.message.answer(text="Добро пожаловать в бот Академии Infinity ☺",
                                  reply_markup=await start_menu_buttons(call.from_user.id))
    await state.finish()


@dp.message_handler(Text(equals=[sign_in, sign_in_ru]))
async def sign_in_function_1(msg: types.Message, state: FSMContext):
    await state.set_state('sign_in_1')
    if msg.text == sign_in:
        await msg.answer(text="Telefon raqamingizni kiriting 📲\n\nNamuna: +998977771188",
                         reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer(text="Введите свой номер телефона 📲\n\nПример: +998977771188",
                         reply_markup=await back_main_menu_button(msg.from_user.id))


@dp.message_handler(state='sign_in_1')
async def sign_in_function_2(msg: types.Message, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/phone_number/{msg.text}/").content)
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail'] and validate_phone_number(msg.text):
            if tg_user['language'] == 'uz':
                await msg.answer(text="""
Bu telefon raqami ro'yhatdan o'tmagan ❌

Telefon raqamingizni kiriting 📲            

Namuna: +998977771188""")
            else:
                await msg.answer(text="""
Этот номер телефона не зарегистрирован ❌

Введите свой номер телефона 📲

Пример: +998977771188""")
        else:
            if tg_user['language'] == 'uz':
                await msg.answer(text="""
Telefon raqam noto'g'ri formatda ❌

Telefon raqamingizni kiriting 📲

Namuna: +998977771188""")
            else:
                await msg.answer(text="""
Номер телефона указан в неправильном формате ❌

Введите свой номер телефона 📲

Пример: +998977771188.""")
    except KeyError:
        if user['chat_id'] != '0':
            if tg_user['language'] == 'uz':
                await msg.answer(text="""
Bu hisob band ✅

Telefon raqamingizni kiriting 📲

Namuna: +998977771188""")
            else:
                await msg.answer("""
Этот аккаунт занят ✅

Введите свой номер телефона 📲

Пример: +998977771188.""")
        else:
            async with state.proxy() as data:
                data['user'] = user
            await state.set_state('sign_in_2')
            if tg_user['language'] == 'uz':
                await msg.answer(text="Parolingizni kiriting 📝")
            else:
                await msg.answer(text="Введите свой пароль 📝")


@dp.message_handler(state='sign_in_2')
async def sign_in_function_3(msg: types.Message, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    async with state.proxy() as data:
        pass
    if msg.text != data['user']['password']:
        if tg_user['language'] == 'uz':
            await msg.answer(text="Parol xato ❌\n\nQaytadan kiriting 📝")
        else:
            await msg.answer(text="Ошибка пароля ❌\n\nПовторите 📝")
    else:
        if tg_user['language'] == 'uz':
            await msg.answer(text="Kirish amalga oshirildi ✅", reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer(text="Вход выполнен ✅", reply_markup=await main_menu_buttons(msg.from_user.id))
        await state.finish()
        requests.patch(url=f"http://127.0.0.1:8000/students/update/{data['user']['id']}/",
                       data={'chat_id': str(msg.from_user.id)})


@dp.message_handler(Text(equals=[sign_up, sign_up_ru]))
async def sign_up_function_1(msg: types.Message, state: FSMContext):
    await state.set_state("sign_up_1")
    if msg.text == log_out:
        await msg.answer(text="Telefon raqamingizni kiriting 📲\n\nNamuna: +998977771188",
                         reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer(text="Введите свой номер телефона 📲\n\nПример: +998977771188",
                         reply_markup=await back_main_menu_button(msg.from_user.id))


@dp.message_handler(state='sign_up_1')
async def sign_up_function_2(msg: types.Message, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/phone_number/{msg.text}/").content)
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    try:
        if validate_phone_number(msg.text) and user['detail']:
            if tg_user['language'] == 'uz':
                await msg.answer(text="Tez orada siz bilan aloqaga chiqamiz 😊",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
            else:
                await msg.answer(text="Мы скоро свяжемся с вами 😊",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
            await state.finish()
            for admin in admins:
                await bot.send_message(text=msg.text, chat_id=admin)
        else:
            if tg_user['language'] == 'uz':
                await msg.answer(text="""
Telefon raqam noto'g'ri formatda ❌

Telefon raqamingizni kiriting 📲

Namuna: +998977771188""")
            else:
                await msg.answer(text="""
Номер телефона указан в неправильном формате ❌

Введите свой номер телефона 📲

Пример: +998977771188.""")
    except KeyError:
        if tg_user['language'] == 'uz':
            await msg.answer(text="""
Bu telefon raqami ro'yhatdan o'tgan ️✅

Telefon raqamingizni kiriting 📲

Namuna: +998977771188""")
        else:
            await msg.answer(text="""
Этот номер телефона зарегистрирован ✅

Введите свой номер телефона 📲

Пример: +998977771188.""")


@dp.message_handler(Text(equals=[log_out, log_out_ru]))
async def log_out_handler(msg: types.Message):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            if msg.text == log_out:
                await msg.answer(text="Avval kirish bosqichini amalga oshiring ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
            else:
                await msg.answer(text="Сначала выполните вход в систему ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
    except KeyError:
        if msg.text == log_out:
            await msg.answer(text="Chiqish amalga oshirildi ✅", reply_markup=await start_menu_buttons(msg.from_user.id))
        else:
            await msg.answer(text="Оформление заказа завершено ✅",
                             reply_markup=await start_menu_buttons(msg.from_user.id))
        requests.patch(url=f"http://127.0.0.1:8000/students/update/{user['id']}/",
                       data={'chat_id': '0'})


@dp.message_handler(Text(equals=[choice_language, choice_language_ru]))
async def change_language_function_1(msg: types.Message, state: FSMContext):
    await state.set_state('language_2')
    if msg.text == choice_language:
        await msg.answer(text="Tilni tanlang", reply_markup=await language_buttons())
    else:
        await msg.answer(text="Выберите язык", reply_markup=await language_buttons())


@dp.callback_query_handler(Text(startswith='language_'), state='language_2')
async def language_function_1(call: types.CallbackQuery, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    data = {
        "chat_id": str(call.from_user.id),
        "username": call.from_user.username,
        "full_name": call.from_user.full_name,
        "language": call.data.split("_")[-1]
    }
    requests.put(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data)
    await call.message.delete()
    if call.data.split("_")[-1] == 'uz':
        await call.message.answer(text="Til o'zgartirildi 🇺🇿", reply_markup=await main_menu_buttons(call.from_user.id))
    else:
        await call.message.answer(text="Язык изменен 🇷🇺", reply_markup=await main_menu_buttons(call.from_user.id))
    await state.finish()
