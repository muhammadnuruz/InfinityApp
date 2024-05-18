import json

import requests
from aiogram.types import ReplyKeyboardMarkup

from bot.buttons.text import back_main_menu, adverts, none_advert, forward_advert, sign_in, sign_up, account, log_out, \
    back_admin_menu, statistic, send_statistic, shop, account_ru, \
    statistic_ru, shop_ru, log_out_ru, sign_up_ru, sign_in_ru, back_main_menu_ru, choice_language, \
    choice_language_ru, month_statistic


async def main_menu_buttons(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [
            [account, statistic],
            [shop],
            [log_out, choice_language]
        ]
    else:
        design = [
            [account_ru, statistic_ru],
            [shop_ru],
            [log_out_ru, choice_language_ru]
        ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def start_menu_buttons(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [
            [sign_in, sign_up]
        ]
    else:
        design = [
            [sign_in_ru, sign_up_ru]
        ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [[back_main_menu]]
    else:
        design = [[back_main_menu_ru]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_admin_menu_button():
    design = [[back_admin_menu]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def admin_menu_buttons():
    design = [
        [adverts, send_statistic],
        [month_statistic],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def advert_menu_buttons():
    design = [
        [none_advert, forward_advert],
        [back_admin_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
