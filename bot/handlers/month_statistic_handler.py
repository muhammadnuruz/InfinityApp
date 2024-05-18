import datetime
import json
import os

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import ChatNotFound

from bot.buttons.functions import create_statistic_image
from bot.buttons.inline_buttons import month_statistic_buttons
from bot.buttons.reply_buttons import back_admin_menu_button, admin_menu_buttons
from bot.buttons.text import month_statistic
from bot.dispatcher import dp, bot
from main import admins

MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


@dp.message_handler(Text(month_statistic))
async def month_statistic_function_1(msg: types.Message, state: FSMContext):
    if msg.from_user.id in admins:
        await state.set_state("month_statistic_1")
        await msg.answer(text="Qaysi guruhni 1 oylik statistikasini olmoxchisiz ❓",
                         reply_markup=await month_statistic_buttons())
        await msg.answer(text="Guruhni tanlang ☝", reply_markup=await back_admin_menu_button())


@dp.callback_query_handler(state='month_statistic_1')
async def month_statistic_function_2(call: types.CallbackQuery, state: FSMContext):
    month_lessons = json.loads(requests.get(url=f"http://127.0.0.1:8000/lessons/month_statistic/{call.data}/").content)
    if month_lessons['count'] == 0:
        await call.message.delete()
        await state.set_state("month_statistic_1")
        await call.message.answer(text="""
Bu guruhda o'tgan oyda dars bo'lmagan ❗

Qaysi guruhni 1 oylik statistikasini olmoxchisiz ❓""", reply_markup=await month_statistic_buttons())
        await call.message.answer(text="Guruhni tanlang ☝", reply_markup=await back_admin_menu_button())
    else:
        group = json.loads(requests.get(url=f"http://127.0.0.1:8000/groups/{call.data}/").content)
        d = {}
        for i in month_lessons['results']:
            d.update({i['name'] + ' ' + i['surname']: i['average_evaluation']})
        date_object = datetime.datetime.now()
        year = date_object.year
        month = date_object.month
        if month == 1:
            previous_month = 12
            previous_year = year - 1
        else:
            previous_month = month - 1
            previous_year = year
        previous_month_name = MONTH_NAMES[previous_month]
        create_statistic_image(data=d, chat_id=call.from_user.id,
                               name=f"{group['group']['name']} - {previous_month_name}",
                               date=f"{previous_year}")
        await call.message.delete()
        await call.message.answer_photo(photo=open(f"images/{call.from_user.id}.png", "rb"),
                                        reply_markup=await admin_menu_buttons())
        await call.answer(text="Statistika guruhga yuborildi ✅", show_alert=True)
        try:
            await bot.send_photo(chat_id=int(group['group']['group_id']),
                                 photo=open(f"images/{call.from_user.id}.png", "rb"))
        except Exception:
            pass
        os.remove(f"images/{call.from_user.id}.png")
        await state.finish()
