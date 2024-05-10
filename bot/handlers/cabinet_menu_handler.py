import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import start_menu_buttons
from bot.buttons.text import account, account_ru
from bot.dispatcher import dp


@dp.message_handler(Text(equals=[account, account_ru]))
async def cabinet_menu_function_1(msg: types.Message):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            if msg.text == account:
                await msg.answer(text="Avval kirish bosqichini amalga oshiring ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
            else:
                await msg.answer(text="Сначала выполните вход в систему ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
    except KeyError:
        group = json.loads(requests.get(url=f"http://127.0.0.1:8000/groups/{user['group']}/").content)
        if msg.text == account:
            await msg.answer(text=f"""
Ism: {user['name']}
Familiya: {user['surname']}
Telefon raqam: {user['phone_number']}
Infin: {user['infin']}
Guruh: {group['group']['name']}
Parol: {user['password']}
""")
        else:
            await msg.answer(text=f"""
Имя: {user['name']}
Фамилия: {user['surname']}
Номер телефона: {user['phone_number']}
Инфин: {user['infin']}
Группа: {group['group']['name']}
Пароль: {user['password']}""")
