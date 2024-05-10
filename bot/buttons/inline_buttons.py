import json

import requests
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.buttons.text import uz_language, ru_language


async def send_statistic_buttons():
    lessons = json.loads(requests.get(url=f"http://127.0.0.1:8000/lessons/unfinished_filter/").content)
    design = []
    for i in lessons['results']:
        group = json.loads(requests.get(url=f"http://127.0.0.1:8000/groups/{i['group']}/").content)
        text = group['group']['name'] + ' ' + i['name']
        design.append([InlineKeyboardButton(text=text, callback_data=i['id'])])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def shop_buttons():
    products = json.loads(requests.get(url=f"http://127.0.0.1:8000/products/").content)
    design = []
    for i in products['results']:
        design.append([InlineKeyboardButton(text=i['name'], callback_data=i['id'])])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def books_for_test_menu_button(text: str):
    lessons = json.loads(requests.get(url=f"http://127.0.0.1:8000/books/{text}/").content)
    design = []
    for i in lessons['results']:
        design.append([InlineKeyboardButton(text=i['name'], callback_data=f"book_for_test-{i['id']}")])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def language_buttons():
    design = [
        [InlineKeyboardButton(text=uz_language, callback_data='language_uz'),
         InlineKeyboardButton(text=ru_language, callback_data='language_ru')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)