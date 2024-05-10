import json
import os

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.functions import create_statistic_image
from bot.buttons.reply_buttons import start_menu_buttons
from bot.buttons.text import statistic, statistic_ru
from bot.dispatcher import dp


@dp.message_handler(Text(equals=[statistic, statistic_ru]))
async def get_statistic_function_1(msg: types.Message):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            if msg.text == statistic:
                await msg.answer(text="Avval kirish bosqichini amalga oshiring ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
            else:
                await msg.answer(text="Сначала выполните вход в систему ☺",
                                 reply_markup=await start_menu_buttons(msg.from_user.id))
    except KeyError:
        statistics = json.loads(
            requests.get(f"http://127.0.0.1:8000/lessons/statistic_filter/{msg.from_user.id}/").content)
        if statistics['count'] == 0:
            if msg.text == statistic:
                await msg.answer(text="Siz hali bironta darsda qatnashmagansiz ❗")
            else:
                await msg.answer(text="Вы еще не посетили ни одного урока ❗")
        else:
            s = 0
            for i in statistics['results']:
                s += i['evaluation']
            create_statistic_image(data={user['name'] + ' ' + user['surname']: s // statistics['count']},
                                   chat_id=msg.from_user.id)
            if msg.text == statistic:
                await msg.answer_photo(photo=open(f"images/{msg.from_user.id}.png", "rb"),
                                       caption=f"{user['name'] + ' ' + user['surname']}ning statistikasi")
            else:
                await msg.answer_photo(photo=open(f"images/{msg.from_user.id}.png", "rb"),
                                       caption=f"Статистика {user['name'] + 'а ' + user['surname']}")
            os.remove(f"images/{msg.from_user.id}.png")
